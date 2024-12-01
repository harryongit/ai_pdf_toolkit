from PyPDF2 import PdfFileReader, PdfFileWriter
import os

async def delete_pdf_pages(file, page_numbers):
    pdf_reader = PdfFileReader(file.file)
    pdf_writer = PdfFileWriter()

    total_pages = pdf_reader.getNumPages()
    for page_num in range(total_pages):
        if page_num not in page_numbers:
            pdf_writer.addPage(pdf_reader.getPage(page_num))

    output_file = os.path.join("temp_files", "deleted_pages_output.pdf")
    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    return output_file
