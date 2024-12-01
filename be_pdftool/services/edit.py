from PyPDF2 import PdfReader, PdfWriter

def delete_pages(input_path: str, output_path: str, pages_to_delete: list) -> bool:
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for i, page in enumerate(reader.pages):
            if i not in pages_to_delete:
                writer.add_page(page)

        with open(output_path, "wb") as f_out:
            writer.write(f_out)
        return True
    except Exception as e:
        print(f"Error editing PDF: {e}")
        return False
