import json

def load_habits():
    try:
        with open("habits.json", "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def save_habits(habits):
    with open("habits.json", "w", encoding="utf-8") as json_file:
        json.dump(habits, json_file, indent=4, ensure_ascii=False)