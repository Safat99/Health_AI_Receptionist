class FaceDetectionError(Exception):
    """Exception raised for errors in the face detection process."""
    def __init__(self, message = None, status_code = None):
        self.message = message
        self.status_code = status_code or 400
        super().__init__(self)
    
    def __str__(self):
        return self.message or "FaceDetectionError occurred"
    
    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv

class CameraError(FaceDetectionError):
    """Exception raised when the camera cannot be accessed."""
    pass

class DirectoryError(FaceDetectionError):
    """Exception raised when directory creation fails."""
    pass

class LoadImageError(FaceDetectionError):
    """Exception raised when load image fails"""
    pass