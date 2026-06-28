from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Project folders
DATA_DIR = ROOT_DIR / "data"
MODELS_DIR = ROOT_DIR / "models"
DOCS_DIR = ROOT_DIR / "docs"
BENCHMARKS_DIR = ROOT_DIR / "benchmarks"

# Default image size
IMAGE_SIZE = (32, 32)

# Supported image formats
SUPPORTED_FORMATS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tiff",
    ".webp",
}

CIFAR10_CLASSES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]