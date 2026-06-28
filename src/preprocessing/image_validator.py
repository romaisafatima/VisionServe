from pathlib import Path

from src.config import settings
from src.logger import get_logger

logger = get_logger(__name__)


def validate_image_path(image_path: str) -> bool:
    """Validate an image file path before loading."""

    path = Path(image_path)

    if not path.exists():
        logger.error(f"Image does not exist: {path}")
        return False

    if path.stat().st_size == 0:
        logger.error(f"Image file is empty: {path}")
        return False

    if path.suffix.lower() not in settings.supported_formats:
        logger.error(f"Unsupported image format: {path.suffix}")
        return False

    max_size_mb = 10
    file_size_mb = path.stat().st_size / (1024 * 1024)

    if file_size_mb > max_size_mb:
        logger.error(f"Image too large: {file_size_mb:.2f} MB")
        return False

    logger.info(f"Image path validated: {path.name}")
    return True