## This is a sample code for face_detection not written by me.
## But working and superbly useful!

import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection.
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Initialize webcam feed.
cap = cv2.VideoCapture(-1)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Convert the image color back so it can be displayed.
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw face detections of each face.
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

    # Display the image.
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to exit.
        break

cap.release()
cv2.destroyAllWindows()
