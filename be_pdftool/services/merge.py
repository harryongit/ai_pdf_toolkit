from PyPDF2 import PdfFileMerger
import os

async def merge_pdfs(files):
    pdf_merger = PdfFileMerger()

    for file in files:
        pdf_merger.append(file.file)

    output_file = os.path.join("temp_files", "merged_output.pdf")
    with open(output_file, "wb") as output_pdf:
        pdf_merger.write(output_pdf)

    return output_file
