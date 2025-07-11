from fastapi import FastAPI
from routes import skin, heart, diabetes, drug, chatbot


app = FastAPI(title="AI Doctor Backend")

app.include_router(skin.router)
app.include_router(heart.router)
app.include_router(diabetes.router)
app.include_router(drug.router)
app.include_router(chatbot.router)

# =============== 2. routes/skin.py ===============
from fastapi import APIRouter, UploadFile, File
from models.skin_model import predict_skin_disease

router = APIRouter(prefix="/skin")

@router.post("/diagnose")
async def diagnose_skin(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict_skin_disease(image_bytes)
    return {"diagnosis": result}