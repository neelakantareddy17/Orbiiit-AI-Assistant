import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "academic_calendar.json")

def academic_tool(query: str):
    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    q = query.lower()
    events = data["events"]
    holidays = data["holidays"]
    academic_dates = data["academic_dates"]

    # ---- CLASS START ----
    if "class" in q and ("start" in q or "begin" in q or "when" in q):
        return f"Classes begin on **{academic_dates['classes_begin']}**."

    # ---- CLASS END ----
    if "class" in q and ("end" in q or "over" in q or "finish" in q):
        return f"Classes end on **{academic_dates['class_ends']}**."

    # ---- MID SEM ----
    if "mid" in q or "midsem" in q or "mid sem" in q:
        return f"Mid Semester Exams start on **{events['mid_semester_exams']['start_date']}**."

    # ---- END SEM ----
    if "end sem" in q or "end-sem" in q or "endsem" in q:
        return f"End Semester Exams start on **{events['end_semester_exams']['start_date']}**."

    # ---- SEMESTER REGISTRATION ----
    if "registration" in q or "register" in q:
        return (
            f"Higher semester registration: **{events['semester_registration']['higher_semesters']}**\n"
            f"Next semester registration: **{events['semester_registration']['next_semester']}**"
        )

    # ---- HOLIDAYS ----
    if "holiday" in q or "holidays" in q:
        response = "### 📅 Holidays:\n"
        for name, date in holidays.items():
            response += f"- **{name.replace('_', ' ')}** → {date}\n"
        return response

    # ---- SPORTS MEET ----
    if "sport" in q:
        sm = events["sports_meet"]
        return f"Sports Meet: **{sm['start']} to {sm['end']}**."

    # ---- PROJECT REVIEWS ----
    if "project" in q or "review" in q:
        pr = events["project_reviews"]
        return (
            f"BTP/MS First Review: **{pr['btp_ms_first_review']}**\n"
            f"BTP Hons/MS Final Review Week: **{pr['btp_hons_ms_final_review_week']}**"
        )

    # ---- ATTENDANCE SUBMISSION ----
    if "attendance" in q:
        return f"Attendance submission: **{events['attendance_submission']}**"

    # ---- REPEAT EXAM ----
    if "repeat exam" in q or "reappear" in q:
        return f"Repeat exams begin on **{events['repeat_exam_start']}**"

    # ---- CATCH ALL ----
    return "Sorry, I couldn't find an academic event related to your query."
