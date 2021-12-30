from flask import Blueprint, url_for, redirect, render_template, flash, request
from app.forms import RegisterForm, Loginform, BuyItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Item, User
from app import db

views = Blueprint('views',__name__)

@views.route('/')
def index():
	return render_template('index.html')

@views.route('/market', methods=['GET','POST'])
@login_required
def show_market():
	buyForm = BuyItemForm()

	if request.method == 'POST':
		buyed_item = request.form.get('buyed_item')
		item_obj = Item.query.filter_by(name=buyed_item).first()
		if item_obj:
			item_obj.owner = current_user.id
			current_user.budget -= item_obj.price
			db.session.commit()
	
	items = Item.query.all()
	return render_template('market.html', items=items, buyForm=buyForm)

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

		login_user(new_user)
		flash(f'Account created successfully, welcome {new_user.username}...', category='success')
		
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

@views.route('/logout')
def logout_page():
	logout_user()
	flash('You have been logged out...', category='info')
	return redirect(url_for('views.index'))