# VisionServe

> A production-style image quality assessment API built with FastAPI and OpenCV.

VisionServe analyzes uploaded images and evaluates their visual quality using computer vision techniques. It provides detailed quality metrics, identifies potential issues, and returns actionable recommendations through a REST API.

---

## Features

- Image upload via REST API
- Blur detection
- Brightness analysis
- Contrast analysis
- Resolution analysis
- Overall image quality score
- Quality recommendations
- Interactive Swagger documentation
- Modular and scalable project architecture

---

## Tech Stack

- Python
- FastAPI
- OpenCV
- NumPy
- Uvicorn

---

## Project Structure

```text
VisionServe
│
├── src/
│   ├── api/
│   ├── inference/
│   ├── preprocessing/
│   ├── utils/
│   └── main.py
│
├── data/
├── docs/
├── models/
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/romaisafatima/VisionServe.git
cd VisionServe
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn src.api.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Analyze Image

```
POST /analyze
```

Upload an image using multipart/form-data.

---

## Example Response

```json
{
    "overall_score": 82,
    "overall_quality": "Good",
    "issues": [],
    "recommendations": [],
    "metrics": {
        "brightness": 154.2,
        "blur_score": 201.5,
        "contrast": 61.4,
        "resolution": {
            "width": 1920,
            "height": 1080
        }
    }
}
```

---

## Future Improvements

- Docker support
- Deployment to the cloud
- Machine Learning based quality assessment
- Noise estimation
- Exposure analysis
- Edge density analysis
- Colorfulness analysis

---

## Author

Developed by **Romaisa Fatima**