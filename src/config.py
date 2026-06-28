from dataclasses import dataclass

from src.constants import (
DATA_DIR,
MODELS_DIR,
DOCS_DIR,
BENCHMARKS_DIR,
IMAGE_SIZE,
SUPPORTED_FORMATS,
)

@dataclass(frozen=True)
class Settings:
    """Project configuration."""

    data_dir = DATA_DIR
    models_dir = MODELS_DIR
    docs_dir = DOCS_DIR
    benchmarks_dir = BENCHMARKS_DIR

    image_size = IMAGE_SIZE
    supported_formats = SUPPORTED_FORMATS

settings = Settings()