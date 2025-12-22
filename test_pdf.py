from utils.pdf_parser import extract_text_from_pdf

with open("sample_resume.pdf", "rb") as f:
    text = extract_text_from_pdf(f)

print("Extracted text preview:\n")
print(text[:1000])
