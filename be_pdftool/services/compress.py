import pikepdf
import os

async def compress_pdf(file):
    # Temporary file path to save the compressed PDF
    output_path = os.path.join('temp_files', f"compressed_{file.filename}")
    
    try:
        # Open the original PDF
        with pikepdf.open(file.file) as pdf:
            # Create a new compressed PDF
            pdf.save(output_path, compress_streams=True)
        
        return output_path
    except Exception as e:
        raise Exception(f"Error during compression: {str(e)}")
