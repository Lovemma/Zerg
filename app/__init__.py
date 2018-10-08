# -*- coding: utf-8 -*-

from flask import Flask

from app.models import db
from app.serializer import ma


def create_app():

    app = Flask(__name__, static_folder='./static')
    app.config.from_object('app.config.settings')

    register_blueprint(app)

    init_db(app)
    init_marshmallow(app)


    return app


def register_blueprint(flask_app):
    from app.v1 import create_blueprint
    flask_app.register_blueprint(create_blueprint())


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def init_marshmallow(app):
    ma.init_app(app)
