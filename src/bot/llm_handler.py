import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_model():
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai.GenerativeModel("gemini-flash-latest")

def ask_llm(model, user_input):
    response = model.generate_content(user_input)
    return response.text
