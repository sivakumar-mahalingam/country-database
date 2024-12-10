import json
import os

def load_country_data():
    """Load the country data from the JSON file."""
    file_path = os.path.join(os.path.dirname(__file__), "country_data.json")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
