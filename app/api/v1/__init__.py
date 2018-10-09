# -*- coding: utf-8 -*-
from flask import Blueprint

from . import banner, theme

def create_blueprint_v1():
    blueprint = Blueprint('v1', __name__, url_prefix='/v1')
    banner.api.register(blueprint)
    theme.api.register(blueprint)
    return blueprint


