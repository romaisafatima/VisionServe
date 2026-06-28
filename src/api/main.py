import shutil
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile

from src.inference.quality_analyzer import analyze_quality
from src.preprocessing.image_loader import load_image
from src.preprocessing.image_validator import validate_image_path

app = FastAPI(title="VisionServe Image Quality API")

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
def root():
    with open("src/api/templates/index.html", "r", encoding="utf-8") as file:
        return file.read()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze_image(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if not validate_image_path(str(file_path)):
        return {"error": "Invalid image file"}

    image = load_image(str(file_path))
    result = analyze_quality(image)

    return result