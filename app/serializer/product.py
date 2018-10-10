# -*- coding: utf-8 -*-
from flask import request, url_for
from marshmallow import post_dump
from marshmallow.fields import Decimal

from app.models.product import Product
from . import ma


class ProductSchema(ma.ModelSchema):
    price = Decimal(as_string=True)

    class Meta:
        model = Product

    @post_dump
    def process_url(self, item):
        url = item.get('main_img_url')
        base_api = request.host_url.rstrip('/')
        main_img_url = base_api + url_for('static', filename='images' + url)
        item['main_img_url'] = main_img_url
        return item


class ProductRecentSchema(ProductSchema):
    class Meta:
        fields = ('main_img_url', 'name', 'price')


class PropertySchema(ma.Schema):
    class Meta:
        fields = ('name', 'detail')


class ProductDetailSchema(ProductSchema):
    properties = ma.Nested(PropertySchema, many=True)

    class Meta:
        fields = (
            'main_img_url', 'stock', 'name', 'price',
            'properties'
        )
