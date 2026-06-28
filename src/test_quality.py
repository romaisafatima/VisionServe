from src.preprocessing.image_validator import validate_image_path
from src.preprocessing.image_loader import load_image
from src.inference.quality_analyzer import analyze_quality

image_path = "data/sample_images/test.jpg"

if validate_image_path(image_path):
    image = load_image(image_path)
    result = analyze_quality(image)
    print(result)