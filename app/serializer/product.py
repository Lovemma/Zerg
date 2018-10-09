# -*- coding: utf-8 -*-
from flask import request, url_for
from marshmallow import post_dump
from marshmallow.fields import Decimal

from app import db
from app.models.product import Product
from . import ma


class ProductSchema(ma.ModelSchema):
    price = Decimal(as_string=True)

    class Meta:
        model = Product
        sqla_session = db.session

    @post_dump
    def process_url(self, item):
        url = item.get('main_img_url')
        base_api = request.host_url.rstrip('/')
        item['main_img_url'] = base_api + url_for('static', filename='images' + url)
        return item
