from fastapi import APIRouter, UploadFile, File
from models.skin_model import predict_skin_disease

router = APIRouter(prefix="/skin")  # Bu obyekt bo'lishi kerak

@router.post("/diagnose")
async def diagnose_skin(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict_skin_disease(image_bytes)
    return {"diagnosis": result}
