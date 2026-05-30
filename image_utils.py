import os
import uuid
from PIL import Image

UPLOAD_FOLDER = "uploads"


def create_upload_folder():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_image(uploaded_file):
    """
    Save uploaded image and return path.
    """

    create_upload_folder()

    file_extension = uploaded_file.name.split(".")[-1]

    unique_filename = f"{uuid.uuid4()}.{file_extension}"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def validate_image(uploaded_file):
    """
    Validate uploaded image.
    """

    try:
        Image.open(uploaded_file)
        return True
    except Exception:
        return False