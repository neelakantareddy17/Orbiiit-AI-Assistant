import json
import os

# Compute PROJECT ROOT directory → HiesenBot/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Build correct JSON file path
ACADEMIC_PATH = os.path.join(BASE_DIR, "data", "academic_calendar.json")


def load_academic():
    with open(ACADEMIC_PATH, "r") as f:
        return json.load(f)


ACA = load_academic()


# ---------------------- ACADEMIC LOGIC ---------------------- #

def search_academic(user):
    q = user.lower()

    if "start" in q or "begin" in q:
        return {"classes_begin": ACA["academic_dates"]["classes_begin"]}

    if ("end" in q and "sem" in q) or "class end" in q:
        return {"class_ends": ACA["academic_dates"]["class_ends"]}

    if "mid" in q:
        return {"mid_sem_start": ACA["events"]["mid_semester_exams"]["start_date"]}

    if "endsem" in q:
        return {"end_sem_start": ACA["events"]["end_semester_exams"]["start_date"]}

    if "registration" in q:
        return {"registration": ACA["events"]["semester_registration"]}

    if "sports" in q:
        return {"sports_meet": ACA["events"]["sports_meet"]}

    if "holiday" in q or "holidays" in q:
        return ACA["holidays"]

    if "instructional" in q or "days" in q:
        return {"instructional_days": ACA["instructional_days"]}

    # Default → return whole academic calendar
    return ACA
