import pdfplumber
import docx

# Parse PDF or DOCX resume
def parse_resume(file, file_type):
    if file_type == 'pdf':
        return parse_pdf(file)
    elif file_type == 'docx':
        return parse_docx(file)

def parse_pdf(file):
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def parse_docx(file):
    doc = docx.Document(file)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
