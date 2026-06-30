import json
import os


def load_career(role_name):
    """
    Load career role JSON file
    """

    filename = role_name.lower().replace(" ", "_") + ".json"

    file_path = os.path.join(
        "..",
        "data",
        "career_roles",
        filename
    )

    with open(file_path, "r") as file:

        data = json.load(file)

    return data