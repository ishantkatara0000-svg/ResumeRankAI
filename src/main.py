from parser import extract_text_from_pdf
from preprocess import clean_text
from skill_extractor import extract_skills
from job_parser import read_job_description
from ats_engine import (calculate_ats_score,
                        get_matched_skills,
                        get_missing_skills,
                        calculate_skill_match)



# -----------------------------
# Resume
# -----------------------------

resume_path = "../data/raw/resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

cleaned_resume = clean_text(resume_text)

resume_skills = extract_skills(cleaned_resume)


# -----------------------------
# Job Description
# -----------------------------

job_path = "../data/external/python_developer.txt"

job_text = read_job_description(job_path)

cleaned_job = clean_text(job_text)

job_skills = extract_skills(cleaned_job)


# -----------------------------
# ATS Score
# -----------------------------

ats_score = calculate_ats_score(
    resume_skills,
    job_skills
)
skill_match = calculate_skill_match(
    resume_skills,
    job_skills
)
final_score = round(
    (skill_match*0.7)+(ats_score*0.3),2
)

matched_skills = get_matched_skills(resume_skills,job_skills)
missing_skills = get_missing_skills(resume_skills,job_skills)

# -----------------------------
# Output
# -----------------------------

print("=" * 60)
print("RESUME TEXT")
print("=" * 60)
print(cleaned_resume)

print("\n" + "=" * 60)
print("RESUME SKILLS")
print("=" * 60)

for skill in resume_skills:
    print("✔", skill)


print("\n" + "=" * 60)
print("JOB DESCRIPTION")
print("=" * 60)
print(job_text)


print("\n" + "=" * 60)
print("JOB SKILLS")
print("=" * 60)

for skill in job_skills:
    print("✔", skill)


print("\n" + "=" * 60)
print("ATS SCORE")
print("=" * 60)

print(f"ATS Score : {ats_score}%")

print("\n" + "=" * 60)
print("SKILL MATCH")
print("=" * 60)
print(f"Skill Match : {skill_match}%")

print("\n" + "=" * 60)
print("FINAL ATS SCORE")
print("=" * 60)
print(f"Final ATS Score : {final_score}%")