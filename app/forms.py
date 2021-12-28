from wtforms.validators import Length, EqualTo, Email, DataRequired
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
	username = StringField(label='User Name:', validators=[Length(min=2, max=50), DataRequired()])
	email = StringField(label='Email address:', validators=[Email(), DataRequired()])
	password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
	password2 = PasswordField(label="Confirm password:", validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField(label='Create Account')
