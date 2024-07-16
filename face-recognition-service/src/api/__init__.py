from flask_restx import Api
from src.api.ping import ping_namespace
from src.api.face_detection.api import face_detector_namespace
from src.api.face_detection.exception_handlers import register_face_detection_handlers

api = Api(
    version="1.0.0", 
    title= "Health AI Receptionist Face-Recognition-Service Docs", 
    doc="/docs", 
    prefix="/api/v1"
)

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(face_detector_namespace, path= "/face_detector")

register_face_detection_handlers(api)