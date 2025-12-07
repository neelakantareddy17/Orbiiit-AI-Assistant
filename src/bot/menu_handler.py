import json
import os
from datetime import datetime, timedelta

# Compute PROJECT ROOT directory → HiesenBot/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Correct path to mess_menu.json
MESS_MENU_PATH = os.path.join(BASE_DIR, "data", "mess_menu.json")


def load_mess_menu():
    with open(MESS_MENU_PATH, "r") as f:
        return json.load(f)["menu"]

MESS = load_mess_menu()


# ---------------------- PARSERS ---------------------- #

def parse_day_from_text(text):
    days_map = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday"
    }

    text = text.lower()

    if "today" in text:
        return datetime.now().strftime("%A")

    if "tomorrow" in text:
        return (datetime.now() + timedelta(days=1)).strftime("%A")

    for key in days_map:
        if key in text:
            return days_map[key]

    return None


def parse_meal_from_text(text):
    text = text.lower()
    for meal in ["breakfast", "lunch", "snacks", "dinner"]:
        if meal in text:
            return meal.capitalize()
    return None


# ---------------------- MENU LOGIC ---------------------- #

def get_mess_menu(user_input):
    day = parse_day_from_text(user_input)
    meal = parse_meal_from_text(user_input)

    # If only meal is asked → assume today
    if meal and not day:
        day = datetime.now().strftime("%A")

    # If no day and no meal → return full menu
    if not day and not meal:
        return MESS

    # Get full day's menu
    daily_menu = MESS.get(day)
    if not daily_menu:
        return f"No menu found for {day}"

    # If only day asked → return full day
    if day and not meal:
        return daily_menu

    # Specific meal for the day
    return {meal: daily_menu.get(meal)}
