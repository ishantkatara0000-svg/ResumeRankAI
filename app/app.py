from flask import Flask, render_template, request
import os
import sys

# src folder ko import path me add karna
sys.path.append("../src")

# Resume Modules
from parser import extract_text_from_pdf
from preprocess import clean_text
from skill_extractor import extract_skills
from name_extractor import extract_name

# Career Modules
from career_loader import load_career
from career_analyzer import analyze_career

app = Flask(__name__)

# Upload Folder
UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():

    return render_template("index.html")

# -----------------------------
# Analyze Resume
# -----------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    # Resume Upload
    resume = request.files["resume"]

    # Career Role
    career_role = request.form["career_role"]

    # Save Resume
    resume_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(resume_path)

    # -----------------------------
    # Resume Pipeline
    # -----------------------------

    # Extract Resume Text
    resume_text = extract_text_from_pdf(
        resume_path
    )

    # Extract Candidate Name
    candidate_name = extract_name(
        resume_text
    )

    # Clean Resume
    cleaned_resume = clean_text(
        resume_text
    )

    # Resume Skills
    resume_skills = extract_skills(
        cleaned_resume
    )

    # -----------------------------
    # Career Pipeline
    # -----------------------------

    career = load_career(
        career_role
    )

    analysis = analyze_career(
        resume_skills,
        career
    )

    readiness = analysis["readiness"]

    matched_skills = analysis["matched_skills"]

    missing_skills = analysis["missing_skills"]

    projects = analysis["projects"]

    tools = analysis["tools"]

    certifications = analysis["certifications"]

    courses = analysis["courses"]
    companies = analysis["companies"]
    interview_questions = analysis["interview_questions"]
    roadmap = analysis["roadmap"]
    ai_tips = analysis["ai_tips"]
 
    salary = analysis["salary"]

# -----------------------------
    # Current Level
    # -----------------------------

    if readiness < 30:

        current_level = "Beginner"

    elif readiness < 60:

        current_level = "Intermediate"

    elif readiness < 85:

        current_level = "Advanced"

    else:

        current_level = "Job Ready"

    # -----------------------------
    # Motivation Message
    # -----------------------------

    if readiness >= 85:

        message = "🔥 You're Job Ready!"

    elif readiness >= 60:

        message = "🚀 Almost Ready"

    elif readiness >= 40:

        message = "💪 Keep Learning"

    else:

        message = "📚 Just Getting Started"

    # -----------------------------
    # User Object
    # -----------------------------

    user = {

        "name": candidate_name,

        "career": career_role,

        "level": current_level,

        "readiness": readiness

    }

    # -----------------------------
    # Dashboard
    # -----------------------------

    return render_template(

        "dashboard.html",

        user=user,

        analysis=analysis,

        resume_skills=resume_skills,

        matched_skills=matched_skills,

        missing_skills=missing_skills,

        projects=projects,

        tools=tools,

        certifications=certifications,

        salary=salary,

        message=message,

        courses=courses,

        companies=companies,

        interview_questions=interview_questions,

        roadmap=roadmap,

        ai_tips=ai_tips,

    )


# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":

    app.run(debug=True)