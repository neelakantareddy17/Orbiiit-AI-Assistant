import sys
import os

# Fix Python path so Streamlit can find bot modules in /src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import streamlit as st
from bot.menu_handler import get_mess_menu
from bot.academic_handler import search_academic
from bot.intent_classifier import classify_intent
from bot.llm_handler import setup_model, ask_llm


# ---------------- SETUP ---------------- #

model = setup_model()

st.set_page_config(page_title="HiesenBot", page_icon="🤖")

st.markdown("<h1 style='text-align: center;'>🤖 HiesenBot – IIIT Kottayam Assistant</h1>", 
            unsafe_allow_html=True)


# ---------------- CHAT HISTORY ---------------- #

if "chat" not in st.session_state:
    st.session_state.chat = []

for sender, message in st.session_state.chat:
    if sender == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)


# ---------------- USER INPUT ---------------- #

user_input = st.chat_input("Ask me anything...")

if user_input:
    # Save user message
    st.session_state.chat.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    # Classify intent
    intent = classify_intent(user_input)

    if intent == "mess":
        reply = get_mess_menu(user_input)

    elif intent == "academic":
        reply = search_academic(user_input)

    else:
        reply = ask_llm(model, user_input)

    # Save bot reply
    st.session_state.chat.append(("assistant", str(reply)))
    st.chat_message("assistant").markdown(str(reply))
