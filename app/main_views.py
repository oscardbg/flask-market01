from flask import Blueprint, request, render_template

main_views = Blueprint('main_views',__name__)

@main_views.route('/')
def index():
	return render_template('index.html')