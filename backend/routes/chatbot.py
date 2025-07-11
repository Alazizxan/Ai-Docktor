from fastapi import APIRouter
from pydantic import BaseModel
import g4f

router = APIRouter(prefix="/chat")

class ChatPrompt(BaseModel):
    message: str

doctor_intro = (
    "Siz professional shifokor-salomatlik bo'yicha maslahatchisiz. "
    "Foydalanuvchi simptomlarini tahlil qilib, tashxis va maslahat bering. "
    "Iltimos, aniq va sodda tilda yordam bering."
)

@router.post("/")
def chat(prompt: ChatPrompt):
    # g4f.ChatCompletion.create orqali so'rov yuborish
    full_prompt = doctor_intro + "\n\n" + prompt.message
    response = g4f.ChatCompletion.create(
        model="gpt-4o-mini",  # istalgan modelni tanlashingiz mumkin
        messages=[{"role": "user", "content": full_prompt}]
    )
    return {"reply": response}
