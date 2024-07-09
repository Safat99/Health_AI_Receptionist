import cv2
import os
import mediapipe as mp
import argparse
import logging
from src.common.exceptions import CameraError, FaceDetectionError, DirectoryError
import src.face_detection.utils as utils

logging.basicConfig(level= logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class FaceDetector:
    """The main class of the face-detection
    """
    def __init__(self):
        # Initialize MediaPipe Face Detection.
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_detection = self.mp_face_detection.FaceDetection(
            min_detection_confidence=0.5)
    
    def detect_faces_mp(self, image):
        """
        tells whether the input images has faces, also gives you the number of faces

        Args:
            image (_type_): an cv2 image

        Returns:
            a boolean field
            if true then the processed-image and the total number of faces
            if false then none, none
        """
    
        converted_image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(converted_image)
        
        if results.detections:
            return True, results, len(results.detections)
        else:
            return False, None, 0
    
    def count_faces_mp(self, image):
        converted_image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(converted_image)
        
        if results.detections:
            return len(results.detections)
        else:
            return 0
        
    def draw_faces_mp(self, image, mp_processing_results):
        """Draw the face detections of each face"""
        if mp_processing_results.detections:
            for detection in mp_processing_results.detections:
                self.mp_drawing.draw_detection(image, detection)
        else:
            raise ValueError
    
    def display_image(self, image):
        """Display the image"""
        cv2.imshow('Face Detection', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows

    def store_faces_for_training_from_camera(self, location):
        """
        Capture and store faces from the camera for training

        Args:
            location (str): Directory to save the captured image. It will be under dataset/ directory.
        """
        
        try:
            cap = utils.initialize_camera()
            utils.create_directory(location)
        except (CameraError, DirectoryError) as e:
            logger.error(e)
            return
                
        frame_count = 0
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break

            # Convert the BGR image to RGB.
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.face_detection.process(image)

            # Convert back to BGR for OpenCV
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.detections:
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = image.shape
                    x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                    face_image = image[y:y+h, x:x+w]    
                    
                    try:
                        cv2.imwrite(os.path.join(location, f"face_{frame_count}.jpg"), face_image)
                    except Exception as e:
                        raise FaceDetectionError(f"Failed to save image '{os.path.join(location, f'face_{frame_count}.jpg')}': {str(e)}")
                    
                    frame_count += 1
                    logger.info("saved %d images for training..",frame_count)


            if frame_count >= 50:  # Save 50 face images, you can change this number
                break
            
        cap.release()
                
        
def main():
    """Main entry point for face detection when called from the terminal."""

    parser = argparse.ArgumentParser(description="Detect faces in the given image or store faces for training from camera")
    parser.add_argument("-i", '--image_path', type=str, help="Path to the input image")
    parser.add_argument("--store", action='store_true', help="to tell whether we are ready to call the 'store_faces_for_training_from_camera' function", required=False)
    parser.add_argument("--location", type=str, help="Folder location to save faces of images")
    
    args = parser.parse_args()
    
    face_detector = FaceDetector()
    
    if args.store:
        if args.location:
            face_detector.store_faces_for_training_from_camera(args.location)
        else:
            print("Error: Folder location must be provided when using --store flag.")
    
    else:
        if not args.image_path:
            print("Error: Image path must be provided if not using --store flag")
            return
        
        image = cv2.imread(args.image_path)

        if image is None:
            print(f"Error: Unable to load image from {args.image_path}")
            return
        
        #detect faces
        is_detected, detected_faces, face_count = face_detector.detect_faces_mp(image)
        
        if not is_detected:
            print(f"Error: Unable to detect any face from {args.image_path}")
        else:
            print(f"Total {face_count} faces found in the image")
            face_detector.draw_faces_mp(image, detected_faces)
            face_detector.display_image(image)

if __name__ == '__main__':
    main()