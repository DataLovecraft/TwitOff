'''
Main application for TwitOff
'''
import os
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
from .twitter add_or_update_user

#basedir = basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    '''
    Create and configure an instance of a flask application
    '''
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['ENV'] = config('ENV') # change to production later
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/user', methods=['POST', 'GET'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or reques.values['user_name']
        try:
            if request.method = 'POST':
                add_or_update_user(name)
                message = 'User {} successfully added!'.format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = 'Error adding {}: {}'.format(name, e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets, message=message)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset', users=[])
    return app
