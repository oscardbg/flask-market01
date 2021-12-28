from app.config import Config
from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	return app