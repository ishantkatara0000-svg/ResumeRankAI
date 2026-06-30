"""
ATS Engine

This module is responsible for

1. ATS Score
2. Matched Skills
3. Missing Skills
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_skills, job_skills):
    """
    Calculate ATS Score using only extracted skills.
    """

    resume_text = " ".join(resume_skills)
    job_text = " ".join(job_skills)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_text])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)


def get_matched_skills(resume_skills, job_skills):
    """
    Return matched skills.
    """

    return sorted(list(set(resume_skills) & set(job_skills)))


def get_missing_skills(resume_skills, job_skills):
    """
    Return missing skills.
    """

    return sorted(list(set(job_skills) - set(resume_skills)))

def calculate_skill_match(resume_skills,job_skills):
    """
    Calculate skill Match Percentage.
    """
    matched = set(resume_skills) & set(job_skills)
    return round((len(matched)/len(job_skills)) * 100,2)