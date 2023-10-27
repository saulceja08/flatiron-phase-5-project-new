#!/usr/bin/env python3

#Remember to export FLASK_RUN_PORT=5555 // export FLASK_APP=server/app.py
#pipenv install && pipenv shell || python server/app.py || npm start --prefix client

# Standard library imports

# Remote library imports
from flask import request, flash, redirect
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, url_for
from forms import RegisterUserForm, LoginUseForm

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!
app = Flask(__name__)
app.config['SECRET_KEY'] = '1b4c68cff7ac17414ad4fd0b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    posts = db.relationship('Post', backref='gamer', lazy=True) #lazy

    def __repr__(self):
        return f"User Info:('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    content= db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post Info:('{self.title}', '{self.date_posted}', '{self.content}')"

tests = [
    {
        'gamer': 'Saul Ceja',
        'video_game': 'Call of Duty: MW3',
        'content': 'Acheived veteran rank!',
        'date_posted': 'October 3, 2023'
    },
    {
        'gamer': 'Eder Macias',
        'video_game': 'Call of Duty: MW3',
        'content': 'Acheived a 15 kill streak',
        'date_posted': 'October 4, 2023'
    },
    {
        'gamer': 'Bryant Urenda',
        'video_game': 'Call of Duty: MW3',
        'content': 'Acheived 3 blood thirsties in 5 minutes',
        'date_posted': 'October 4, 2023'
    },
    {
        'gamer': 'Guillermo Ceja',
        'video_game': 'Call of Duty: MW3',
        'content': 'Acheived level 100 in Zombies solo',                   
        'date_posted': 'October 2, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', tests=tests, title='Game Home Page') 

@app.route('/about')
def about():
    return render_template('about.html', tests=tests, title='Gaming About Page')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterUserForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('registration.html', title='Registration', form=form)

@app.route('/login')
def login():
    form = LoginUseForm
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

