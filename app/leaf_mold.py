from fastapi import FastAPI, File, UploadFile
import uvicorn
from io import BytesIO
import random
import tensorflow as tf
import numpy as np
from PIL import Image

app = FastAPI()

MODEL = tf.keras.models.load_model("../saved_models/2")
CLASS_NAMES = ["Bacterial_Spot","Leaf_Mold", "Healthy"]

@app.get("/")
async def ping():
    return {'disease':random.choice(CLASS_NAMES),
    'model_version':random.randint(0,9)}

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())

    img_batch = np.expand_dims(image,0)

    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])

    return{
        'class':predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost',port=8000)
