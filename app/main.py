import os
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

app = Blueprint('app', __name__)

# route and function to handle the home page
@app.route('/')
def index():
    return render_template('index.html')

# route and function to handle the profile page, note login required.
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# route and function to handle the about page
@app.route('/about')
def about():
    return render_template('about.html')

# route and function to handle the license page
@app.route('/license')
def license():
    return render_template('license.html')