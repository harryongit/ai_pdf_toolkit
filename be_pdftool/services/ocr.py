import pytesseract
from PIL import Image
from pdf2image import convert_from_path

def perform_ocr(input_path: str) -> str:
    try:
        images = convert_from_path(input_path)
        extracted_text = ""

        for img in images:
            text = pytesseract.image_to_string(img)
            extracted_text += text + "\n"

        return extracted_text
    except Exception as e:
        print(f"Error performing OCR: {e}")
        return ""
