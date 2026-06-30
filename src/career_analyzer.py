def analyze_career(resume_skills, career_data):
    """
    Compare Resume Skills with Career Skills
    """

    required_skills = career_data["skills"]

    matched_skills = []

    missing_skills = []

    for skill in required_skills:

        if skill.lower() in [s.lower() for s in resume_skills]:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    readiness = round(
        (len(matched_skills) / len(required_skills)) * 100,
        2
    )

    return {

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "readiness": readiness,

        "projects": career_data["projects"],

        "tools": career_data["tools"],

        "certifications": career_data["certifications"],

        "salary": career_data["salary"]

    }