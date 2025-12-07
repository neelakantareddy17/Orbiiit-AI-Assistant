from bot.menu_handler import get_mess_menu
from bot.academic_handler import search_academic
from bot.intent_classifier import classify_intent
from bot.llm_handler import setup_model, ask_llm

def chat():
    model = setup_model()
    print("\n🤖 HiesenBot ready! Type 'exit' to quit.\n")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("👋 Goodbye!")
            break

        intent = classify_intent(user)

        if intent == "mess":
            print("\n🍽️ Mess Info:", get_mess_menu(user), "\n")
        elif intent == "academic":
            print("\n📅 Academic Info:", search_academic(user), "\n")
        else:
            print("\nHiesenBot:", ask_llm(model, user), "\n")

if __name__ == "__main__":
    chat()
