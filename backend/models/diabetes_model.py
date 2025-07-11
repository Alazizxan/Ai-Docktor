import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models_saved", "diabetes_model.pkl")



model = joblib.load(MODEL_PATH)

def predict_diabetes(data):
    x = [[
        data['Pregnancies'],
        data['Glucose'],
        data['BloodPressure'],
        data['SkinThickness'],
        data['Insulin'],
        data['BMI'],
        data['DiabetesPedigreeFunction'],
        data['Age']
    ]]
    prob = model.predict_proba(x)[0][1]
    return round(prob, 3)
