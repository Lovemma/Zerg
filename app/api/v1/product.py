# -*- coding: utf-8 -*-
from flask import jsonify

from app.libs.redprint import Redprint
from app.models.product import Product
from app.serializer.product import ProductSchema

api = Redprint('product')


@api.route('/recent', methods=['GET'])
def read_recent_product():
    products = Product.query.limit(15).all()
    if products is not None:
        product_schema = ProductSchema(many=True)
        result = product_schema.dump(products).data
        return jsonify(result)
    else:
        return jsonify({})
