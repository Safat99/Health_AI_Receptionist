from flask_restx import Api
from src.api.ping import ping_namespace

api = Api(version="1.0.0", title= "Health AI Receptionist Face-Recognition-Service Docs", doc="/docs", prefix="/api/v1")

api.add_namespace(ping_namespace, path="/ping")