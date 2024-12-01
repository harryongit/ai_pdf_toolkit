from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from services import compress, convert, edit, merge, ocr, watermark, sign, unlock, protect, flatten, scan
import logging
import os

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper function to get the temporary file path
def get_temp_file_path(filename):
    return os.path.join('temp_files', filename)

@app.post("/compress_pdf")
async def compress_pdf(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for compression")
        result_path = await compress.compress_pdf(file)
        logger.info(f"File compressed and saved to {result_path}")
        return FileResponse(result_path, filename="compressed_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during compression: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/convert_pdf_to_word")
async def convert_pdf_to_word(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for conversion to Word")
        result_path = await convert.convert_pdf_to_word(file)
        logger.info(f"File converted to Word and saved to {result_path}")
        return FileResponse(result_path, filename="converted_" + file.filename.split('.')[0] + ".docx", media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    except Exception as e:
        logger.error(f"Error during conversion: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/edit_pdf")
async def edit_pdf(content: str, file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for editing with content: {content}")
        result_path = await edit.edit_pdf(file, content)
        logger.info(f"File edited and saved to {result_path}")
        return FileResponse(result_path, filename="edited_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during editing: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/merge_pdfs")
async def merge_pdfs(files: list[UploadFile] = File(...)):
    try:
        logger.info(f"Received {len(files)} files for merging")
        result_path = await merge.merge_pdfs(files)
        logger.info(f"Files merged and saved to {result_path}")
        return FileResponse(result_path, filename="merged_output.pdf", media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during merging: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/ocr_pdf")
async def ocr_pdf(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for OCR processing")
        result_path = await ocr.ocr_pdf(file)
        logger.info(f"OCR completed and saved to {result_path}")
        return FileResponse(result_path, filename="ocr_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during OCR: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/watermark_pdf")
async def watermark_pdf(file: UploadFile = File(...), watermark_text: str = "Sample Watermark"):
    try:
        logger.info(f"Received file: {file.filename} for watermarking")
        result_path = await watermark.add_watermark(file, watermark_text)
        logger.info(f"Watermarked file saved to {result_path}")
        return FileResponse(result_path, filename="watermarked_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during watermarking: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/sign_pdf")
async def sign_pdf(file: UploadFile = File(...), signature_image: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for signing")
        result_path = await sign.sign_pdf(file, signature_image)
        logger.info(f"Signed file saved to {result_path}")
        return FileResponse(result_path, filename="signed_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during signing: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/unlock_pdf")
async def unlock_pdf(file: UploadFile = File(...), password: str = "default"):
    try:
        logger.info(f"Received file: {file.filename} for unlocking")
        result_path = await unlock.unlock_pdf(file, password)
        logger.info(f"Unlocked file saved to {result_path}")
        return FileResponse(result_path, filename="unlocked_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during unlocking: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/protect_pdf")
async def protect_pdf(file: UploadFile = File(...), password: str = "default"):
    try:
        logger.info(f"Received file: {file.filename} for protecting")
        result_path = await protect.protect_pdf(file, password)
        logger.info(f"Protected file saved to {result_path}")
        return FileResponse(result_path, filename="protected_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during protecting: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/flatten_pdf")
async def flatten_pdf(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for flattening")
        result_path = await flatten.flatten_pdf(file)
        logger.info(f"Flattened file saved to {result_path}")
        return FileResponse(result_path, filename="flattened_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during flattening: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/scan_pdf")
async def scan_pdf(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename} for scanning")
        result_path = await scan.scan_pdf(file)
        logger.info(f"Scanned file saved to {result_path}")
        return FileResponse(result_path, filename="scanned_" + file.filename, media_type="application/pdf")
    except Exception as e:
        logger.error(f"Error during scanning: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
