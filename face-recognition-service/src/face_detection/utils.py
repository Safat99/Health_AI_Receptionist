import os
from src.common.exceptions import CameraError, DirectoryError
import cv2

def initialize_camera():
    cap = cv2.VideoCapture(-1)
    if not cap.isOpened():
        raise CameraError("Camera not found or cannot be opened.")
    return cap

def create_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    except Exception as e:
        raise DirectoryError(f"Failed to create directory {path}: {str(e)}")