from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, UnidentifiedImageError
import numpy as np
import io
import torch

app = FastAPI(title="EuroSAT Land Cover API")

# Replace "*" with your website's origin before production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model once.
model = torch.load("eurosat_clf.pkl", map_location=torch.device("cpu"), weights_only=False)
model.eval()


@app.get("/")
def home():
    return {"message": "EuroSAT Land Cover API is running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    if file.content_type not in {
        "image/jpeg",
        "image/png",
        "image/webp"
    }:
        raise HTTPException(
            status_code=415,
            detail="Upload a JPG, PNG, or WebP image."
        )

    try:
        image_bytes = await file.read()
        image = Image.open(
            io.BytesIO(image_bytes)
        ).convert("RGB")

    except (UnidentifiedImageError, OSError):
        raise HTTPException(
            status_code=400,
            detail="Invalid image file."
        )

    # IMPORTANT:
    # This preprocessing is only an example.
    # It must match the preprocessing used during training.
    image = image.resize((64, 64))

    image_array = np.asarray(image, dtype=np.float32)

    # Example for a classifier trained on flattened RGB pixels.
    features = image_array.reshape(1, -1)

    try:
        prediction = model.predict(features)[0]

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=(
                "Prediction failed. Check the model's expected "
                "input features and preprocessing."
            )
        ) from exc

    return {
        "filename": file.filename,
        "prediction": str(prediction)
    }