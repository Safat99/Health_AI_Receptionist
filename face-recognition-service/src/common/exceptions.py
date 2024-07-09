class FaceDetectionError(Exception):
    """Exception raised for errors in the face detection process."""
    pass

class CameraError(FaceDetectionError):
    """Exception raised when the camera cannot be accessed."""
    pass

class DirectoryError(FaceDetectionError):
    """Exception raised when directory creation fails."""
    pass
