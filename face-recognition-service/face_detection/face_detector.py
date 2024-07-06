import cv2
import mediapipe as mp
import argparse

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
        
def main():
    """if the FaceDetector python file is called from terminal"""

    parser = argparse.ArgumentParser(description="Detect faces in the given image")
    parser.add_argument("-i", '--image_path', type=str, help="Path to the input image")
    
    args = parser.parse_args()
    
    face_detector = FaceDetector()
    
    image = cv2.imread(args.image_path)

    if image is None:
        print(f"Error: Unable to load image from {args.image_path}")
        return
    
    #detect faces
    is_detected, detected_faces, face_count = face_detector.detect_faces_mp(image)
    
    if not is_detected:
        print(f"Error: Unable to detect any face from {args.image_path}")
    else:
        print(f"total {face_count} faces found in the image")
        face_detector.draw_faces_mp(image, detected_faces)
        
    face_detector.display_image(image)
        
if __name__ == "__main__":
    main()