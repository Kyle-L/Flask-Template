import os
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

# route and function to handle the home page
@main.route('/')
def index():
    return render_template('index.html')

# route and function to handle the profile page, note login required.
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# route and function to handle the about page
@main.route('/about')
def about():
    return render_template('about.html')

# route and function to handle the license page
@main.route('/license')
def license():
    return render_template('license.html')