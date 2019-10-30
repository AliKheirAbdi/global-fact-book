from flask import Flask
from app.config import config_options




def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    return app

