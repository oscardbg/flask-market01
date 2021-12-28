from flask import Blueprint, request, render_template
from app.forms import RegisterForm

views = Blueprint('views',__name__)

@views.route('/')
def index():
	return render_template('index.html')

@views.route('/register')
def show_register():
	form = RegisterForm()
	
	return render_template('register.html', form=form)