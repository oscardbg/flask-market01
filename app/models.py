from app import db, bcrypt, lmanager
from flask_login import UserMixin

@lmanager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(length=50), unique=True)
	email = db.Column(db.String(length=50), unique=True)
	password_hash = db.Column(db.String(length=80))
	budget = db.Column(db.Integer(), default=1000)
	items = db.relationship('Item', backref='user', lazy=True)

	@property
	def frt_budget(self):
		if len(str(self.budget)) >= 4:
			return f'$ {str(self.budget)[:-3]},{str(self.budget)[-3:]}'
		else:
			return f'${self.budget} '

	@property
	def password(self):
		return self.password

	@password.setter
	def password(self, txt_password):
		self.password_hash = bcrypt.generate_password_hash(txt_password).decode('utf-8')

	def check_password_crt(self, req_password):
		return bcrypt.check_password_hash(self.password_hash, req_password)
			
	def __str__(self):
		return f'User: {self.username}'

	def can_purchase(self, item_obj):
		return self.budget >= item_obj.price
	
class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=50), unique=True)
	price = db.Column(db.Integer())
	barcode = db.Column(db.String(length=20), unique=True)
	description = db.Column(db.String(length=1024), unique=True)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __str__(self):
		return f'Item: {self.name}'