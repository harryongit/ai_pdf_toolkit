import os
from fastapi import UploadFile

def save_temp_file(upload_file: UploadFile, temp_dir: str) -> str:
    """Save an uploaded file to a temporary directory and return its path."""
    file_path = os.path.join(temp_dir, upload_file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return file_path
