from flask import Blueprint, url_for, redirect, render_template, flash
from app.forms import RegisterForm
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
		
		new_user = User(username=usr, email=mail, password_hash=passwd)
		db.session.add(new_user)
		db.session.commit()
		
		return redirect(url_for('views.show_market'))

	if form.errors != {}:
		for err_msg in form.errors.values():
			flash(f'There was an error creating the user: {err_msg}', category='danger')
	
	return render_template('register.html', form=form)