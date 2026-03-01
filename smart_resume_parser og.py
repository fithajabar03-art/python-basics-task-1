import re
import fitz  
import docx
def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text() 
    return text
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_sections(text):
    sections = {}
    current_section = None

    lines = text.split("\n")

    for line in lines:
        clean_line = line.strip()
        if clean_line.isupper() and len(clean_line) > 3:
           current_section = clean_line
           sections[current_section] = []
        elif current_section:
            sections[current_section].append(clean_line)

    return sections

def extract_skills(sections):
    skills = []
    if "TECHNICAL SKILLS" in sections:
        for line in sections["TECHNICAL SKILLS"]:
            if ":" in line:
                _, skill_part = line.split(":", 1)
                skills.extend([s.strip() for s in skill_part.split(",")])
    return skills

    
def extract_education(sections):
     if "EDUCATION" in sections:
        return [line for line in sections["EDUCATION"] if line]
     return []

def extract_experience(sections):
  if "EXPERIENCE" in sections:
        return [line for line in sections["EXPERIENCE"] if line]
  return []

def parse_resume(file, file_type):
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file)
    else:
        return None

    text = clean_text(text)

    return {
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Experience": extract_experience(text)
    }

