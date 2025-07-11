from fastapi import APIRouter
from pydantic import BaseModel
from models.heart_model import predict_heart

router = APIRouter(prefix="/heart")

class HeartInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@router.post("/predict")
def predict(data: HeartInput):
    return {"heart_attack_risk": predict_heart(data.dict())}
