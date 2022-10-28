from flask import Flask
from pony.flask import Pony

app = Flask(__name__)
Pony(app)

@app.route("/")
def hello_world():
    return "Hello, World."
