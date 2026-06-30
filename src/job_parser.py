def read_job_description(file_path):
    """
    Read Job Description text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:

        text = file.read()

    return text