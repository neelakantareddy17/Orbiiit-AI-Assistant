def classify_intent(q):
    q = q.lower()

    if any(word in q for word in ["mess", "menu", "breakfast", "lunch", "snacks", "dinner"]):
        return "mess"

    if any(word in q for word in ["academic", "holiday", "calendar", "exam", "sem", "class"]):
        return "academic"

    return "general"
