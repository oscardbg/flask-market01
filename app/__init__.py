from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from app.config import Config
from os.path import exists
from flask import Flask

db = SQLAlchemy()
DB_NAME = 'market.db'

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)

	from app.views import views
	from app.models import User,Item
	
	app.register_blueprint(views, url_prefix='/')
	
	create_db(app)
	
	admin = Admin(app)
	admin.add_view(ModelView(User, db.session))
	admin.add_view(ModelView(Item, db.session))

	return app

def create_db(app):
	if not exists('app/' + DB_NAME):
		db.create_all(app=app)
		print(' * Database created...')