from pathlib import Path

from src.inference.onnx_model import ONNXModel
from src.logger import get_logger

logger = get_logger(__name__)

ONNX_MODEL_PATH = Path("models/exported/model.onnx")


class DummyModel:
    """Temporary model until ONNX model is available."""

    def predict(self, image):
        return {"label": "sharp", "confidence": 0.75}


def load_model():
    """Load ONNX model if available, otherwise use dummy model."""

    if ONNX_MODEL_PATH.exists():
        logger.info(f"Loading ONNX model: {ONNX_MODEL_PATH}")
        model = ONNXModel(str(ONNX_MODEL_PATH))
        logger.info("ONNX model loaded successfully.")
        return model

    logger.warning("ONNX model not found. Falling back to dummy model.")
    return DummyModel()