import os
from flask import Flask, render_template, request

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

app = Flask(__name__)

# route and function to handle the home page
@app.route('/')
def index():
    return render_template('index.html')

# route and function to handle the home page
@app.route('/about')
def about():
    return render_template('about.html')

# route and function to handle the home page
@app.route('/license')
def license():
    return render_template('license.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host= '0.0.0.0')