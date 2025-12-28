# Orbiiit Campus AI Assistant

A FastAPI-based AI chatbot designed for campus and student-support use cases. The assistant provides short, friendly, and humorous responses (typically 40–60 words) and integrates with a Next.js frontend deployed on Vercel. The backend is deployed on Render with secure CORS support for both local and production environments.

## 🎯 Objectives

- Provide a lightweight conversational assistant for campus and student queries  
- Deliver concise, helpful answers instead of long explanations  
- Support seamless integration between FastAPI, LLM agent logic, and a web frontend  

## 🚀 Features

- FastAPI backend with LLM response generation through `build_agent`
- Short, humorous, user-friendly replies (~40–60 words)
- Dynamic CORS handling (localhost + production domain)
- REST API endpoint for chatbot integration
- Production-ready deployment setup (Render + Vercel)

## 🧩 Tech Stack

- Backend: FastAPI, Python  
- AI Layer: Custom agent (`src.agent.build_agent`)  
- Deployment: Render (API) + Vercel (Frontend)  
- Data Format: JSON-based request/response  

## 📡 API Endpoint

### POST /askme

Request
{
"message": "your question here"
}

Response
{
"reply": "AI generated response"
}

The backend automatically applies tone, brevity, and humor constraints.

## 🛠 Local Development

1. Install dependencies  
pip install -r requirements.txt

2. Run the FastAPI server  
uvicorn api:app --reload

Server runs at  
http://127.0.0.1:8000

## 🌍 Deployment

- Backend: Render  
- Frontend: Vercel (https://orbiiit.vercel.app)  
- CORS configured for:
  - http://localhost:3000  
  - http://127.0.0.1:3000  
  - https://orbiiit.vercel.app  

Additional domains can be added as needed.

## 🧱 Project Structure (Simplified)

src/
└── agent/ # LLM agent logic
api.py # FastAPI application + chatbot endpoint
requirements.txt
README.md

## 📌 Roadmap

- Conversation memory / history mode  
- Multiple tone presets (formal, casual, academic)  
- Admin dashboard & analytics  
- Role-based authentication  
- Support for multi-campus deployments  

## 🧾 License

This project is intended for learning and demonstration purposes within campus and academic environments. Licensing terms may be expanded as the project evolves.

## 💡 Acknowledgements

Thanks to the contributors and collaborators working on the Orbiiit ecosystem and supporting the development of AI-based student assistance tools.
