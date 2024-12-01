from PyPDF2 import PdfFileReader, PdfFileWriter
import os

async def extract_pdf_pages(file, page_numbers):
    pdf_reader = PdfFileReader(file.file)
    pdf_writer = PdfFileWriter()

    for page_num in page_numbers:
        if page_num < pdf_reader.getNumPages():
            pdf_writer.addPage(pdf_reader.getPage(page_num))

    output_file = os.path.join("temp_files", "extracted_pages_output.pdf")
    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    return output_file
