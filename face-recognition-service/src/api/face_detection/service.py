from src.face_detection.face_detector import FaceDetector
from src.common.exceptions import LoadImageError, FaceDetectionError




class FaceDetectionService:
    def __init__(self):
        self.face_detector = FaceDetector()
    
    def detect_faces(self, image_file: str):
        """Detect faces in the given image file"""        
        try:
            is_detected, _, face_count = self.face_detector.detect_faces_mp(image_path=image_file)
            if not is_detected:
                raise FaceDetectionError(f"No face detected from {image_file}")
            return face_count
        except LoadImageError as e:
            raise LoadImageError(e.message, 400)
        except Exception as e:
            raise FaceDetectionError(e.message)
            
    
    def store_faces_from_image(self, image_file, destinaiton_location):
        """Store faces from a single image file"""
        self.face_detector.store_faces_for_training_from_single_image(image_file, destinaiton_location)
        return {'message' : 'stored faces succesfully'}
        
    def store_faces_from_folder(self, source_folder_path, destination_location):
        """Store faces from iamges in a folder"""
        self.face_detector.store_faces_for_training_from_folder(source_folder_path, destination_location)
        return {'message' : 'stored faces to {destination_folder} successfully'}