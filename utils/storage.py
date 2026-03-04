import json
import os

FILE_PATH = "data/database.json"

def load_data():

    if not os.path.exists(FILE_PATH):
        return {"users": [], "projects": [], "tasks": []}

    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)

    except:
        return {"users": [], "projects": [], "tasks": []}


def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)