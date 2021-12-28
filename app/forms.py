from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from app.models import User

class RegisterForm(FlaskForm):

	def validate_username(self, user_to_check):
		user = User.query.filter_by(username=user_to_check.data).first()
		if user:
			raise ValidationError('Username already exists, please try another name')

	def validate_email(self, mail_to_check):
		mail = User.query.filter_by(email=mail_to_check.data).first()
		if mail:
			raise ValidationError('Email address already exists, please try another email')

	username = StringField(label='User Name:', validators=[Length(min=2, max=50), DataRequired()])
	email = StringField(label='Email address:', validators=[Email(), DataRequired()])
	password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
	password2 = PasswordField(label="Confirm password:", validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField(label='Create Account')
