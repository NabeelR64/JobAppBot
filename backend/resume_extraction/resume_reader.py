import os
from pdfminer.high_level import extract_text
import nltk
import re

import ssl

PHONE_REG = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
 
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('all')
# nltk.download('punkt_tab')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
 
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
 
 
# def extract_text_from_docx(docx_path):
#     txt = docx2txt.process(docx_path)
#     if txt:
#         return txt.replace('\t', ' ')
#     return None
 
 
def extract_names(txt):
    person_names = []
 
    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent, language='english', preserve_line=True))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )
 
    return person_names


def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
    if phone:
        number = ''.join(phone[0])
 
        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None
 
 
if __name__ == '__main__':
    resume_dir = '/Users/nrahman/workspace/github.com/NabeelR64/JobAppBot/backend/resume_extraction/resumes'
    for resume in os.listdir(resume_dir):
        resume_path = os.path.join(resume_dir, resume)
        text = extract_text_from_pdf(resume_path)
        names = extract_names(text)
        phone_number = extract_phone_number(text)
        print('resume:', resume)
        if names:
            print('name:', names[0])  # noqa: T001
        if phone_number:
            print('ph:', phone_number)

