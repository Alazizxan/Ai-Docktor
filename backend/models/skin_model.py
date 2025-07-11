from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = os.path.join(BASE_DIR, "models_saved", "xception_skin_model.h5")





model = load_model(MODEL_PATH)

IMG_SIZE = 224  # Model uchun kerakli o'lcham

def predict_skin_disease(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize

    preds = model.predict(img_array)
    # Faraz qilamiz 2 class: [Benign, Malignant]
    class_idx = np.argmax(preds, axis=1)[0]

    return "Benign" if class_idx == 0 else "Malignant"
