from src.inference.model_loader import load_model
from src.logger import get_logger
from src.startup import create_project_directories

logger = get_logger(__name__)

def main() -> None:
    logger.info("======================================")
    logger.info(" VisionServe")
    logger.info(" Production ML Inference System")
    logger.info("======================================")

    create_project_directories()
    model = load_model()
    logger.info(f"Active model: {model.__class__.__name__}")

    logger.info("Application started successfully.")


if __name__ == "__main__":
    main()