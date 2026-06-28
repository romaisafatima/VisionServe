from pathlib import Path
from typing import Any


def _calculate_aspect_ratio(width: int, height: int) -> float:
    """Calculate image aspect ratio."""

    return round(width / height, 2)


def get_image_info(image: Any, image_path: str) -> dict:
    """Extract information from an image."""

    height, width = image.shape[:2]

    if len(image.shape) == 2:
        channels = 1
    else:
        channels = image.shape[2]

    path = Path(image_path)

    return {
        "filename": path.name,
        "width": width,
        "height": height,
        "channels": channels,
        "aspect_ratio": _calculate_aspect_ratio(width, height),
    }