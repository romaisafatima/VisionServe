from dataclasses import dataclass


@dataclass
class ImageInfo:
    """Information about an image."""

    filename: str
    width: int
    height: int
    channels: int
    aspect_ratio: float