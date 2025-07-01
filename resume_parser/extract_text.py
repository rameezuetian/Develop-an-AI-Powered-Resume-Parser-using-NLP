# parser/extract_text.py

import os
import docx
from pdfminer.high_level import extract_text as extract_pdf_text


def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_text_from_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    
    if ext == '.pdf':
        return extract_pdf_text(path)
    elif ext == '.docx':
        return extract_text_from_docx(path)
    elif ext == '.txt':
        return extract_text_from_txt(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
