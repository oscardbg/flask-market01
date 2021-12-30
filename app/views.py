from flask import Blueprint, url_for, redirect, render_template, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegisterForm, Loginform, BuyItemForm, SellItemForm
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
	sellForm = SellItemForm()

	if request.method == 'POST':

		# Item buying code
		buyed_item = request.form.get('buyed_item')
		itemb_obj = Item.query.filter_by(name=buyed_item).first()
		if itemb_obj:
			if current_user.can_purchase(itemb_obj):
				itemb_obj.buy(current_user)
				flash(f'Congrats, you bought {itemb_obj.name} for $ {itemb_obj.price}', category='success')
			else:
				flash(f'Not enough money to buy {itemb_obj.name}', category='danger')

		# Item selling code
		selled_item = request.form.get('selled_item')
		items_obj = Item.query.filter_by(name=selled_item).first()
		if items_obj:
			if current_user.can_sell(items_obj):
				items_obj.sell(current_user)
				flash(f'Congrats, you sold {items_obj.name} back to market', category='success')
			else:
				flash(f'Something went wrong trying to sell {items_obj.name}', category='danger')
	
		return redirect(url_for('views.show_market'))

	items = Item.query.filter_by(owner=None)
	owned = Item.query.filter_by(owner=current_user.id)
	return render_template('market.html', items=items, owned=owned, buyForm=buyForm, sellForm=sellForm)

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