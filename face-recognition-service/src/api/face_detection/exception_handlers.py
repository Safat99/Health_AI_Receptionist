from flask import jsonify
from flask_restx import Api
from src.common.exceptions import LoadImageError, FaceDetectionError, DirectoryError, CameraError
import logging

logging.basicConfig(level= logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def register_face_detection_handlers(api: Api):
    @api.errorhandler(LoadImageError)
    def handle_load_image_error(error):
        logger.error(f"LoadImageError: {error.message}")
        response = jsonify({
            'message' : error.message,
            'code' : error.status_code,
            'name' : 'LoadImageError'
        })
        # response = error.to_dict() 
        # # if returning the response obj
        response.status_code = error.status_code
        return response.json, response.status_code

    @api.errorhandler(FaceDetectionError)
    def handle_face_detection_error(error):
        logger.error(f"FaceDetectionError: {str(error)}")
        response = jsonify({
            'message': error.message,
            'name' : 'FaceDetectionError',
            'code' : 404
            })
        response.status_code = 404
        return response.json, response.status_code

    @api.errorhandler(DirectoryError)
    def handle_directory_error(error):
        logger.error(f"DirectoryError: {str(error)}")
        response = jsonify({
            'message': str(error),
            'name' : 'DirectoryError',
            'code' : 405
            })
        response.status_code = 405
        return response.json, response.status_code
    
    @api.errorhandler(CameraError)
    def handle_camera_error(error):
        logger.error(f"CameraError: {str(error)}")
        response = jsonify({
            'message': str(error),
            'name' : 'CameraError',
            'code' : 400
            })
        response.status_code = 400
        return response.json, response.status_code

