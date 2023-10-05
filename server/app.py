#!/usr/bin/env python3

#Remember to export FLASK_RUN_PORT=5555 // export FLASK_APP=server/app.py
#pipenv install && pipenv shell || python server/app.py || npm start --prefix client

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource
from flask import Flask, render_template

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') #, posts = posts

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

