import os
import sys
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

# Fix import paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_DIR)

from agent import build_agent

agent = build_agent()

st.set_page_config(page_title="HiesenBot", page_icon="🤖")
st.title("🤖 HiesenBot – IIIT Kottayam Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []

for sender, msg in st.session_state.chat:
    st.chat_message(sender).markdown(msg)

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

    reply = agent(user_input)
    st.session_state.chat.append(("assistant", reply))
    st.chat_message("assistant").markdown(reply)
