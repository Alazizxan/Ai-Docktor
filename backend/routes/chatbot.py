from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import process_user_message

router = APIRouter(prefix="/chat", tags=["Chatbot"])

class ChatPrompt(BaseModel):
    user_id: str
    message: str

@router.post("/")
def chat(prompt: ChatPrompt):
    """
    Foydalanuvchi xabarini chatbotga yuboradi va javobni qaytaradi.
    """
    return process_user_message(prompt.user_id, prompt.message)
