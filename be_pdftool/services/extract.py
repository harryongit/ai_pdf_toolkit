from PyPDF2 import PdfReader, PdfWriter

def extract_pdf_pages(input_path: str, output_path: str, pages_to_extract: list) -> bool:
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for i in pages_to_extract:
            writer.add_page(reader.pages[i])

        with open(output_path, "wb") as f:
            writer.write(f)
        return True
    except Exception as e:
        print(f"Error extracting pages from PDF: {e}")
        return False
