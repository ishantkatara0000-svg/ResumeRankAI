def analyze_career(resume_skills, career_data):
    """
    Analyze Resume against Career Role
    """

    required_skills = career_data.get("skills", [])

    matched_skills = []

    missing_skills = []

    resume_lower = [skill.lower() for skill in resume_skills]

    for skill in required_skills:

        if skill.lower() in resume_lower:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    if len(required_skills) == 0:

        readiness = 0

    else:

        readiness = round(

            (len(matched_skills) / len(required_skills)) * 100,

            2

        )

    return {

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "readiness": readiness,

        "projects": career_data.get("projects", []),

        "tools": career_data.get("tools", []),

        "courses": career_data.get("courses", []),

        "companies": career_data.get("companies", []),

        "interview_questions": career_data.get("interview_questions", []),

        "roadmap": career_data.get("roadmap", []),

        "ai_tips": career_data.get("ai_tips", []),

        "certifications": career_data.get("certifications", []),

        "salary": career_data.get(

            "salary",

            {

                "fresher": "N/A",

                "experienced": "N/A"

            }

        )

    }