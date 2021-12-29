from flask import Blueprint, url_for, redirect, render_template, flash
from werkzeug.wrappers import request
from app.forms import RegisterForm, Loginform
from flask_login import login_user
from app.models import Item, User
from app import db

views = Blueprint('views',__name__)

@views.route('/')
def index():
	return render_template('index.html')

@views.route('/market')
def show_market():
	items = Item.query.all()
	return render_template('market.html', items=items)

@views.route('/register', methods=['GET','POST'])
def show_register():
	form = RegisterForm()

	if form.validate_on_submit():
		usr = form.username.data
		mail = form.email.data
		passwd = form.password1.data
		
		new_user = User(username=usr, email=mail, password=passwd)
		db.session.add(new_user)
		db.session.commit()
		
		return redirect(url_for('views.show_market'))

	if form.errors != {}:
		for err_msg in form.errors.values():
			flash(f'There was an error creating the user: {err_msg}', category='danger')
	
	return render_template('register.html', form=form)

@views.route('/login', methods=['GET','POST'])
def show_login():
	form = Loginform()

	if form.validate_on_submit():
		req_user = User.query.filter_by(username=form.username.data).first()
		if req_user and req_user.check_password_crt(
			req_password = form.password.data
		):
			login_user(req_user)
			flash(f'You are logged in as: {req_user.username}', category='success')
			return redirect(url_for('views.show_market'))
		else:
			flash(f'Username or password are incorrect, please try again...', category='danger')

	return render_template('login.html', form=form)