'''
Main application for TwitOff
'''
import os
from flask import Flask
from .models import DB

basedir = basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    '''
    Create and configure an instance of a flask app
    '''
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to our app'
    return app
