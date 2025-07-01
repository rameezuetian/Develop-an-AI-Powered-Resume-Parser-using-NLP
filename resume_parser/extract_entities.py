# parser/extract_entities.py

import re
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample skillset to match
SKILL_SET = {
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "tensorflow", "pytorch", "aws", "docker", "linux", "git", "data science",
}

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[\s\-]?)?(\(?\d{3}\)?[\s\-]?)?\d{3}[\s\-]?\d{4}', text)
    return match.group(0) if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    text_lower = text.lower()
    found = [skill for skill in SKILL_SET if skill in text_lower]
    return list(set(found))

def extract_entities(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }
