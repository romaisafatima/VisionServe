import cv2
from pathlib import Path

from src.logger import get_logger

logger = get_logger(__name__)


def load_image(image_path: str):
    """Load an image from disk."""

    image = cv2.imread(str(Path(image_path)))

    if image is None:
        logger.error(f"Unable to load image: {image_path}")
        raise FileNotFoundError(f"Image not found: {image_path}")

    logger.info(f"Image loaded successfully: {image_path}")

    return image