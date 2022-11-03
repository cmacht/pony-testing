from flask import Flask
from pony.flask import Pony
from views import hello

def create_app():
    app = Flask(__name__)
    Pony(app)
    app.register_blueprint(hello.bp)

    return app

