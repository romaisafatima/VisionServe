from src.config import settings
from src.logger import get_logger

logger = get_logger(__name__)


def create_project_directories() -> None:
    """Create required project directories if they don't exist."""

    directories = [
        settings.data_dir,
        settings.models_dir,
        settings.docs_dir,
        settings.benchmarks_dir,
    ]

    for directory in directories:
        directory.mkdir(exist_ok=True)
        logger.info(f"Verified directory: {directory.name}")