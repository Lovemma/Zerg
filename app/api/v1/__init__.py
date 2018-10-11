# -*- coding: utf-8 -*-
from flask import Blueprint

from . import banner, theme, product, category

def create_blueprint_v1():
    blueprint = Blueprint('v1', __name__, url_prefix='/v1')
    banner.api.register(blueprint)
    theme.api.register(blueprint)
    product.api.register(blueprint)
    category.api.register(blueprint)
    return blueprint


