import re


def extract_name(resume_text):
    """
    Extract candidate name from resume.
    """

    lines = resume_text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            if re.match(r"^[A-Za-z ]+$", line):

                return line.title()

    return "Candidate"