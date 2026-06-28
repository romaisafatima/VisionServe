from src.preprocessing.image_validator import validate_image_path
from src.preprocessing.image_loader import load_image
from src.preprocessing.image_info import get_image_info

image_path = "data/sample_images/test.jpg"

if validate_image_path(image_path):
    image = load_image(image_path)
    info = get_image_info(image, image_path)
    print(info)