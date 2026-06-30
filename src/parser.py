"""
parser.py

This module is responsible for extracting text
from Resume PDFs.
"""

import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF resume.

    Parameters:
        pdf_path (str): Path of the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text