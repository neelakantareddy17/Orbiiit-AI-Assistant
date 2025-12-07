# src/test_models.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("GOOGLE_API_KEY set?", bool(api_key))

genai.configure(api_key=api_key)

print("\nListing models visible to this key:\n")
for m in genai.list_models():
    print(m.name, "->", getattr(m, "supported_generation_methods", None))
