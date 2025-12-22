import pdfplumber

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from uploaded PDF resume.
    Returns cleaned text string.
    """

    full_text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    # Basic cleaning
    cleaned_text = (
        full_text
        .replace("\t", " ")
        .replace("•", " ")
        .strip()
    )

    return cleaned_text
