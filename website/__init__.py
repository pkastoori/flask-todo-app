from flask import Flask
import os


def create_app():

    app = Flask(__name__)
    
    from .todo import todo
    app.register_blueprint(todo, url_prefix='/')


    return app