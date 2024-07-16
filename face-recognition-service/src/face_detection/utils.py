import os
from src.common.exceptions import CameraError, DirectoryError, LoadImageError
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

def is_file_image(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png'))

def load_image(image_path:str):
    try:
        if not is_file_image(filename=image_path):
            raise LoadImageError(f" file: {image_path} is not a image")
        image = cv2.imread(image_path)
        if image is None:
            raise LoadImageError(f"Failed to load image {image_path} : Image file not found or cannot be read")        
        return image
    except LoadImageError as e:
        raise LoadImageError(e.message)
    except Exception as e:
        raise LoadImageError(f"load image general exception occured >> Failed to load image {image_path} : {str(e)}")    