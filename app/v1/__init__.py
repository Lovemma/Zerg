# -*- coding: utf-8 -*-
from flask import Blueprint

from . import banner

def create_blueprint():
    blueprint = Blueprint('v1', __name__, url_prefix='/v1')
    banner.api.register(blueprint)
    return blueprint


