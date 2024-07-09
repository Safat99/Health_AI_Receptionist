# from imutils.video import VideoStream # alternate for using pi-camera and threading
import argparse
import imutils
import time
import cv2
import logging


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str,
                default=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml',
                help="path to haar cascade face detector"
                )
args = vars(ap.parse_args())

# loading the cascade classifier from ..
detector = cv2.CascadeClassifier(args["cascade"])

logging.warning("starting video stream...")
# vs = VideoStream(src=0).start()
cap = cv2.VideoCapture(-1)
time.sleep(2.0)

while True:
    # grab the frame, resize and convert it to grayscale
    # frame = vs.read()
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # perform face detection
    rects = detector.detectMultiScale(gray,
                                      scaleFactor=1.05,
                                      minNeighbors=5,
                                      minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE
                                      )

    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255,0), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(5) & 0xFF
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
# vs.stop()