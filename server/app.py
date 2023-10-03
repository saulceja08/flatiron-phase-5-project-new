#!/usr/bin/env python3

#Remember to export FLASK_RUN_PORT=5555 // export FLASK_APP=server/app.py

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Test practice server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

