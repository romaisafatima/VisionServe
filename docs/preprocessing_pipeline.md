# Preprocessing Pipeline

## Responsibilities

### image_loader.py
- Load an image from disk.

### image_validator.py
- Validate file type.
- Check if image is corrupted.

### image_info.py
- Extract image metadata.
- Report dimensions.
- Report channels.
- Report aspect ratio.
- Report file size.

### transforms.py
- Resize image.
- Normalize image.
- Prepare image for inference.