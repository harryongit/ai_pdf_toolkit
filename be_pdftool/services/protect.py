from PyPDF2 import PdfFileReader, PdfFileWriter
import os

async def protect_pdf(file, password):
    pdf_reader = PdfFileReader(file.file)
    pdf_writer = PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page_num))

    output_file = os.path.join("temp_files", "protected_output.pdf")
    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    # Apply password protection
    pdf_writer.encrypt(password)

    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    return output_file
