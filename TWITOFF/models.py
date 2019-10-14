'''
SQLAlchemy models for TwitOff
'''

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class user(DB.Model):
    '''
    Twitter users the we pull and analyze
    '''
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class tweet(DB.Model):
    '''
    Tweets
    '''
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
