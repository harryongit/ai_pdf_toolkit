from PyPDF2 import PdfFileReader, PdfFileWriter
import os

async def split_pdf(file):
    pdf_reader = PdfFileReader(file.file)
    total_pages = pdf_reader.getNumPages()

    output_files = []
    for page_num in range(total_pages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_num))
        
        output_file = os.path.join("temp_files", f"split_page_{page_num + 1}.pdf")
        with open(output_file, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

        output_files.append(output_file)

    return output_files
