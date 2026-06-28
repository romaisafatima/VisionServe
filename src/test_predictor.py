from src.inference.model_loader import load_model
from src.inference.predictor import predict
from src.preprocessing.image_loader import load_image
from src.preprocessing.image_transformer import resize_image, normalize_image, prepare_for_onnx
from src.preprocessing.image_validator import validate_image_path

image_path = "data/sample_images/test.jpg"

if validate_image_path(image_path):
    model = load_model()
    image = load_image(image_path)
    image = resize_image(image)
    image = normalize_image(image)
    image = prepare_for_onnx(image)
    
    prediction = predict(model, image)

    print(prediction)