import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "mess_menu.json")

def mess_menu_tool(query: str):
    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    menu = data["menu"]   # FIXED
    q = query.lower()

    if " " in q:
        q = q.replace("?", "").replace(",", "")

    day = next((d for d in menu if d in q), None)
    meal = next((m for m in ["breakfast", "lunch", "dinner", "snacks"] if m in q), None)

    if not day:
        return "Please specify a weekday."

    if not meal:
        full = menu[day]
        return "Full menu for " + day.title() + ":\n" + "\n".join(f"{k}: {v}" for k, v in full.items())

    return menu[day][meal]
