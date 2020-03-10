import os

from django.conf import settings


def is_valid_image_extension(file_path):
    extension = os.path.splitext(str(file_path).lower())[1]
    return extension in settings.TRIX_EXTENSIONS
