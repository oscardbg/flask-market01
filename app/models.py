from app import db

class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(length=50), unique=True)
	email = db.Column(db.String(length=50), unique=True)
	password_hash = db.Column(db.String(length=80))
	budget = db.Column(db.Integer(), default=1000)
	items = db.relationship('Item', backref='user', lazy=True)

	def __str__(self):
		return f'User: {self.username}'
	
class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=50), unique=True)
	price = db.Column(db.Integer())
	barcode = db.Column(db.String(length=20), unique=True)
	description = db.Column(db.String(length=1024), unique=True)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __str__(self):
		return f'Item: {self.name}'