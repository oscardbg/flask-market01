from flask import Blueprint, request, render_template

views = Blueprint('main_views',__name__)

@views.route('/')
def index():
	return render_template('index.html')