import cv2
import numpy as np

from src.constants import IMAGE_SIZE
from src.logger import get_logger

logger = get_logger(__name__)


def resize_image(image: np.ndarray) -> np.ndarray:
    """Resize image to the model's expected input size."""

    resized = cv2.resize(image, IMAGE_SIZE)

    logger.info(f"Image resized to {IMAGE_SIZE}")

    return resized


def normalize_image(image: np.ndarray) -> np.ndarray:
    """Normalize pixel values to the range [0, 1]."""

    normalized = image / 255.0

    logger.info("Image normalized.")

    return normalized

def prepare_for_onnx(image: np.ndarray) -> np.ndarray:
    """Convert image from HWC to NCHW format for ONNX."""

    # HWC: height, width, channels
    # CHW: channels, height, width
    image = image.transpose(2, 0, 1)

    # NCHW: batch, channels, height, width
    image = np.expand_dims(image, axis=0)

    image = image.astype(np.float32)

    logger.info(f"Image prepared for ONNX with shape: {image.shape}")

    return image