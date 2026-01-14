from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
from freeflow_llm import FreeFlowClient
import os

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def health():
    return { "status": "ok" }

@app.post("/chat")
def chat(
    req: ChatRequest,
    x_api_key: str = Header(None)
):
    # proteção simples entre Laravel -> IA
    if x_api_key != os.getenv("INTERNAL_API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")

    with FreeFlowClient() as client:
        response = client.chat(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente especialista em desenvolvimento "
                        "de software, APIs, Laravel, PHP, Node.js e arquitetura backend."
                    )
                },
                {
                    "role": "user",
                    "content": req.message
                }
            ],
            temperature=0.3
        )

    return {
        "reply": response.content
    }
