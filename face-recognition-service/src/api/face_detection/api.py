from flask_restx import Namespace, Resource, fields
from src.api.face_detection.service import FaceDetectionService
from flask import request

fds = FaceDetectionService()

face_detector_namespace = Namespace('face_detector', description= "Face Detection operations")

image_path_model = face_detector_namespace.model(
    "Detect Face from the given image path",
    {
        "image_path" : fields.String(description = "the path(filename) of the input image"),
    },
)

face_detect_response_model = face_detector_namespace.model(
    "the success response", 
    {
        'faces_count' : fields.Integer(description = "Total number of faces detected in the given image")
    }
)

class DetectFace(Resource):
    @face_detector_namespace.expect(image_path_model)
    @face_detector_namespace.response(200, 'face detected', face_detect_response_model)
    @face_detector_namespace.response(400, 'Face Detection Error')
    def post(self):
        payload = request.get_json()
        image_path = payload.get('image_path')
        face_count = fds.detect_faces(image_file=image_path)
        return {'faces_count' : face_count}, 200

face_detector_namespace.add_resource(DetectFace,"/detect-faces-from-image")