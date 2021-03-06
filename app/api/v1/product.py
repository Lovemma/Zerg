# -*- coding: utf-8 -*-
from flask import jsonify

from app.libs.exceptions import NotFound
from app.libs.redprint import Redprint
from app.models.product import Product
from app.serializer.product import ProductRecentSchema, ProductDetailSchema

api = Redprint('product')


@api.route('/recent', methods=['GET'])
def read_recent_product():
    products = Product.query.limit(15).all()
    if products is not None:
        product_schema = ProductRecentSchema(many=True)
        result = product_schema.dump(products).data
        return jsonify(result)
    else:
        return jsonify({})


@api.route('/<int:product_id>', methods=['GET'])
def read_one_product(product_id):
    product = Product.query.filter_by(id=product_id).first()

    if product is not None:

        product_schema = ProductDetailSchema()
        result = product_schema.dump(product).data

        return jsonify(result)
    else:
        raise NotFound()
