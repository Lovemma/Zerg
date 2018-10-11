# -*- coding: utf-8 -*-

from flask import jsonify

from app.libs.redprint import Redprint
from app.models.category import Category
from app.serializer.category import CategorySchema

api = Redprint('category')


@api.route('', methods=['GET'])
def read_all_category():
    categories = Category.query.all()

    if categories is not None:
        schema = CategorySchema(many=True)
        result = schema.dump(categories).data

        return jsonify(result)
    else:
        return jsonify({})
