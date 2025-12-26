from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import build_agent

app = FastAPI()
agent = build_agent()

class Query(BaseModel):
    message: str

@app.post("/askme")
def ask_me(q: Query):
    reply = agent(q.message)
    return {"reply": reply}
