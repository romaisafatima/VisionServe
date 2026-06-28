import numpy as np
import onnxruntime as ort

from src.constants import CIFAR10_CLASSES
from src.logger import get_logger

logger = get_logger(__name__)


class ONNXModel:
    """Wrapper around an ONNX Runtime inference session."""

    def __init__(self, model_path: str):
        logger.info(f"Creating ONNX session from: {model_path}")

        self.session = ort.InferenceSession(model_path)

        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name

        logger.info(f"ONNX input name: {self.input_name}")
        logger.info(f"ONNX output name: {self.output_name}")

    def predict(self, image):
        """Run prediction using ONNX Runtime."""

        outputs = self.session.run(
            [self.output_name],
            {self.input_name: image},
        )

        logits = outputs[0][0]

        probabilities = np.exp(logits) / np.sum(np.exp(logits))

        predicted_index = int(np.argmax(probabilities))

        return {
            "label": CIFAR10_CLASSES[predicted_index],
            "confidence": float(probabilities[predicted_index]),
        }