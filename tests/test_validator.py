import pytest

from src.constants import SUPPORTED_FORMATS
from src.preprocessing.image_validator import validate_image_path


def test_supported_formats_not_empty():
    """Ensure the application supports at least one image format."""
    assert len(SUPPORTED_FORMATS) > 0


@pytest.mark.parametrize(
    "filename",
    [f"image{ext}" for ext in SUPPORTED_FORMATS],
)
def test_supported_formats(filename):
    """Every supported image format should be accepted."""
    assert validate_image_path(filename)


@pytest.mark.parametrize(
    "filename",
    [
        "image.txt",
        "image.pdf",
        "image.docx",
        "image.exe",
        "image.mp4",
    ],
)
def test_unsupported_formats(filename):
    """Unsupported formats should be rejected."""
    assert not validate_image_path(filename)