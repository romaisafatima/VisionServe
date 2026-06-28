from src.logger import get_logger

logger = get_logger(__name__)


def predict(model, image):
    """Run inference."""

    prediction = model.predict(image)

    logger.info("Prediction completed.")

    return prediction