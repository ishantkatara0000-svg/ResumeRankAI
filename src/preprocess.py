import re


def clean_text(text):
    """
    Clean extracted resume text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove Email
    text = re.sub(r"\S+@\S+", "", text)

    # Remove Phone Number
    text = re.sub(r"\+?\d[\d\s-]{8,}\d", "", text)

    # Remove Special Characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove Extra Spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()