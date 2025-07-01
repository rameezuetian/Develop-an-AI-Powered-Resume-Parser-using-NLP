# parser/extract_experience.py

import re

# Simple job title list (expandable)
TITLES = ["Data Scientist", "Software Engineer", "Machine Learning Engineer", "Research Assistant",
          "AI Engineer", "Developer", "Intern", "Data Analyst"]

def extract_experience(text):
    experiences = []
    
    # Common patterns
    pattern = re.findall(r'(?P<title>[\w\s]+?)\s+(at|@|–|-)\s+(?P<company>[A-Za-z0-9 &]+)[,\s]+(?:\(?)(?P<years>\d{4})(?:\)?)[\s\-–]*(?P<end_year>\d{4}|present|Present)?', text, re.IGNORECASE)

    for match in pattern:
        title, _, company, start_year, end_year = match
        try:
            start = int(start_year)
            end = int(end_year) if end_year.lower() != "present" else 2025
            duration = end - start
        except:
            duration = None
        
        experiences.append({
            "title": title.strip(),
            "company": company.strip(),
            "years": duration
        })

    return experiences
