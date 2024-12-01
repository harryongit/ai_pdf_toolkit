from pdf2docx import Converter
import os

async def convert_pdf_to_word(file):
    input_pdf = file.file
    output_docx = os.path.join("temp_files", "output.docx")
    
    cv = Converter(input_pdf)
    cv.convert(output_docx, start=0, end=None)
    cv.close()

    return output_docx
