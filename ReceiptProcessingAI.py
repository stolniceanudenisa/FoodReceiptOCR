import re
import cv2
import pytesseract
import configparser


class ReceiptProcessingAI:
    def __init__(self):
        # Inițializare configurare pentru Tesseract
        config = configparser.ConfigParser()
        config.read('ConfigFile.properties')
        pytesseract.pytesseract.tesseract_cmd = config['Path']['OCR_reader']

    def process_receipt(self, image_path):
        """
        Procesează un bon alimentar pentru a extrage produsele și totalul.
        :param image_path: calea către imaginea bonului
        :return: dicționar cu produsele și totalul
        """
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ocr_text = pytesseract.image_to_string(gray, config="--psm 6")

        item_names = re.findall(r'\b([a-zA-Z ]+)\b', ocr_text)
        exclude_words = {
            "kg"
        }
        food_items = [
            item.strip() for item in item_names
            if item.strip() and item.strip().lower() not in exclude_words  and len(item.strip()) > 1
        ]

        return food_items


receiptAI = ReceiptProcessingAI()
# image_path = "C:/Users/40766/OneDrive/Desktop/b4.png"
image_path = r"C:\Users\40766\Personal Projects\Ayres-Software-Practica-AI2\Ayres-Software-Practica-AI2\AI\Ayres-Software-Practica-AI\AI\receipts\b1.png"
result = receiptAI.process_receipt(image_path)
print(result)
