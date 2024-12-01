from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def sign_pdf(input_file: str, signature_file: str, output_file: str, page_number: int = 0, x: int = 100, y: int = 100) -> bool:
    """
    Function to apply a digital signature to a PDF using an image.

    Args:
        input_file (str): Path to the input PDF file.
        signature_file (str): Path to the signature image (e.g., PNG or JPG).
        output_file (str): Path to the output signed PDF file.
        page_number (int): Page number where the signature should be placed (default: 0).
        x (int): X-coordinate for the signature placement (default: 100).
        y (int): Y-coordinate for the signature placement (default: 100).

    Returns:
        bool: True if signing was successful, False otherwise.
    """
    try:
        # Read the existing PDF
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()

        # Create a new PDF with the signature
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawImage(signature_file, x, y, width=150, height=50)  # Adjust the size as needed
        can.save()

        # Move the pointer to the beginning of the stream
        packet.seek(0)

        # Merge the signature onto the specified page
        signature_pdf = PdfReader(packet)
        for i, page in enumerate(pdf_reader.pages):
            if i == page_number:
                page.merge_page(signature_pdf.pages[0])
            pdf_writer.add_page(page)

        # Write the updated PDF to the output file
        with open(output_file, "wb") as out_pdf:
            pdf_writer.write(out_pdf)

        return True
    except Exception as e:
        print(f"An error occurred while signing the PDF: {e}")
        return False
