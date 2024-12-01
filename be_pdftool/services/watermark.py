from PyPDF2 import PdfFileReader, PdfFileWriter
import os

async def sign_pdf(file, signature):
    pdf_reader = PdfFileReader(file.file)
    pdf_writer = PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

    output_file = os.path.join("temp_files", "signed_output.pdf")
    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    return output_file
