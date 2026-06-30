from parser import extract_text_from_pdf
from name_extractor import extract_name

resume_path = "../data/raw/resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

name = extract_name(resume_text)

print(name)