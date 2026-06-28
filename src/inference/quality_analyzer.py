import cv2
import numpy as np


def _generate_summary(overall_quality: str, issues: list[str]) -> str:
    if not issues:
        return "The image quality is good with no major detected issues."

    issue_text = ", ".join(issues)
    return f"The image quality is {overall_quality} with detected issues: {issue_text}."


def analyze_quality(image: np.ndarray) -> dict:
    """Analyze image quality using computer vision rules."""

    height, width = image.shape[:2]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    brightness = float(np.mean(gray))
    blur_score = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    contrast = float(np.std(gray))
    saturation = float(np.mean(hsv[:, :, 1]))

    noise_score = float(np.std(gray - cv2.GaussianBlur(gray, (5, 5), 0)))

    edges = cv2.Canny(gray, 100, 200)
    edge_density = float(np.sum(edges > 0) / edges.size)

    b, g, r = cv2.split(image.astype("float"))
    rg = np.abs(r - g)
    yb = np.abs(0.5 * (r + g) - b)
    colorfulness = float(np.sqrt(np.std(rg) ** 2 + np.std(yb) ** 2) + 0.3 * np.sqrt(np.mean(rg) ** 2 + np.mean(yb) ** 2))

    if brightness < 60:
        exposure_status = "underexposed"
    elif brightness > 200:
        exposure_status = "overexposed"
    else:
        exposure_status = "normal"

    issues = []
    recommendations = []

    if blur_score < 100:
        issues.append("blurry")
        recommendations.append("Hold the camera steadier or use autofocus.")

    if exposure_status == "underexposed":
        issues.append("dark")
        recommendations.append("Increase lighting or exposure.")

    if exposure_status == "overexposed":
        issues.append("overexposed")
        recommendations.append("Reduce exposure or avoid harsh direct light.")

    if contrast < 40:
        issues.append("low_contrast")
        recommendations.append("Improve lighting contrast or avoid flat lighting.")

    if width < 640 or height < 480:
        issues.append("low_resolution")
        recommendations.append("Use a higher resolution image.")

    if noise_score > 20:
        issues.append("noisy")
        recommendations.append("Use better lighting or reduce camera ISO.")

    if saturation < 35:
        issues.append("low_saturation")
        recommendations.append("Improve color richness or avoid washed-out lighting.")

    if colorfulness < 20:
        issues.append("low_colorfulness")
        recommendations.append("Use better lighting or a more visually rich scene.")

    score = 100
    score -= 25 if "blurry" in issues else 0
    score -= 20 if "dark" in issues else 0
    score -= 20 if "overexposed" in issues else 0
    score -= 15 if "low_contrast" in issues else 0
    score -= 10 if "low_resolution" in issues else 0
    score -= 15 if "noisy" in issues else 0
    score -= 10 if "low_saturation" in issues else 0
    score -= 10 if "low_colorfulness" in issues else 0

    score = max(score, 0)

    if score >= 80:
        overall_quality = "good"
    elif score >= 50:
        overall_quality = "fair"
    else:
        overall_quality = "poor"

    return {
        "overall_score": score,
        "overall_quality": overall_quality,
        "summary": _generate_summary(overall_quality, issues),
        "issues": issues,
        "recommendations": recommendations,
        "metrics": {
            "brightness": brightness,
            "blur_score": blur_score,
            "contrast": contrast,
            "noise_score": noise_score,
            "exposure_status": exposure_status,
            "colorfulness": colorfulness,
            "edge_density": edge_density,
            "saturation": saturation,
            "resolution": {
                "width": width,
                "height": height,
            },
        },
    }