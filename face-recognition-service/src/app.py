from flask import Flask
from src.config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_by_name[config_name])
    
    from src.api import api
    api.init_app(app)
    
    return app