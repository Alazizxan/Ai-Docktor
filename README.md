# =============== 11. Model fayllar ===============
# models_saved/skin_model.pth     # EfficientNet B0 (Xception yoki B0 variantlar)
# models_saved/heart_model.pkl    # Random Forest yoki XGBoost
# models_saved/diabetes_model.pkl # Logistic Regression

# =============== 12. Ishga tushirish yo‘riqnomasi ===============
# 1. Terminalda: `pip install -r requirements.txt`
# 2. Modellarni `models_saved/` papkaga joylashtiring
# 3. Serverni ishga tushurish: `uvicorn main:app --reload`
# 4. Swagger API: `http://127.0.0.1:8000/docs`
# 5. Test qiling:
#     - POST /skin/diagnose — rasm yuklash
#     - POST /heart/predict — JSON
#     - POST /diabetes/predict — JSON
#     - GET /drug/search?name=paracetamol
#     - POST /chat — GPT API
# .\.venv310\Scripts\Activate.ps1    