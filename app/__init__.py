from app.config import Config
from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	from app.main_views import main_views
	app.register_blueprint(main_views, url_prefix='/')

	return app