import pytesseract
from PIL import Image
import io
import os

async def pdf_scanner(file):
    # Extract text using OCR (requires tesseract to be installed)
    pdf_image = Image.open(file.file)
    text = pytesseract.image_to_string(pdf_image)

    output_text_file = os.path.join("temp_files", "scanned_output.txt")
    with open(output_text_file, "w") as text_file:
        text_file.write(text)

    return output_text_file
