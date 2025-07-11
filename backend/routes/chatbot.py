from fastapi import APIRouter
import openai
import os

router = APIRouter(prefix="/chat")
openai.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/")
def chat(prompt: dict):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt["message"]}]
    )
    return {"reply": response["choices"][0]["message"]["content"]}
