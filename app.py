from flask import Flask

print('')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
