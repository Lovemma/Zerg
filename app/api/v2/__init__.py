# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api



def create_blueprint_v2():
    blueprint = Blueprint('v2', __name__, url_prefix='/v2')
    api = Api(blueprint)
    from app.api.v2.banner import BannerCollection
    api.add_resource(BannerCollection, '/banner', endpoint='banner')

    return blueprint


