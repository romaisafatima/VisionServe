import numpy as np

from src.inference.quality_analyzer import analyze_quality


def test_uniform_image_has_quality_issues():
    """A flat uniform image should be flagged as lower quality."""

    image = np.ones((100, 100, 3), dtype=np.uint8) * 120

    result = analyze_quality(image)

    assert result["overall_quality"] == "fair"
    assert "blurry" in result["issues"]
    assert "low_contrast" in result["issues"]