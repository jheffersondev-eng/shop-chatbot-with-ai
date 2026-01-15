from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from freeflow_llm import FreeFlowClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    with FreeFlowClient() as client:
        response = client.chat(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente especialista em desenvolvimento de software, "
                        "APIs REST, Laravel, PHP, arquitetura MVC, clean code e boas práticas."
                    )
                },
                {
                    "role": "user",
                    "content": req.message
                }
            ]
        )

    return {"reply": response.content}
