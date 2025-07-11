from fastapi import APIRouter
from pydantic import BaseModel
from models.diabetes_model import predict_diabetes

router = APIRouter(prefix="/diabetes")

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@router.post("/predict")
def predict(data: DiabetesInput):
    return {"diabetes_risk": predict_diabetes(data.dict())}
