from flask import Blueprint, render_template

error = Blueprint('errors', __name__)

@error.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404