# pdf.py - models for handling PDF metadata and file operations
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PDF(Base):
    __tablename__ = 'pdf_files'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    filepath = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PDF(filename={self.filename}, filepath={self.filepath}, created_at={self.created_at})>"

    @classmethod
    def create(cls, filename, filepath):
        """
        Creates a new PDF entry in the database
        :param filename: Name of the file
        :param filepath: Path where the file is stored
        :return: The created PDF object
        """
        return cls(filename=filename, filepath=filepath)
