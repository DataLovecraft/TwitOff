# import the flask package
from flask import Flask, render_template

#create a flask web server and instantiate the application
app = (__name__)

# routes determine location
@app.route('/')
def home():
    return render_template('home.html')

@app.route('about')
def about():
    return render_template('about.html')
