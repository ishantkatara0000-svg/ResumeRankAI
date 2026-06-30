# skill_extractor.py

SKILLS = [
    "python",
    "java",
    "c++",
    "javascript",
    "html",
    "css",
    "sql",
    "mongodb",
    "git",
    "github",
    "docker",
    "linux",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "data science",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch"
]


def extract_skills(text):
    """
    Extract technical skills from resume text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))