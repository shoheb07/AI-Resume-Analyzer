import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return set(keywords)

def match_keywords(resume_text, job_desc):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc)

    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords - resume_keywords

    return matched, missing
