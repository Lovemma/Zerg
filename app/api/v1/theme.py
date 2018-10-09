# -*- coding: utf-8 -*-
from flask import jsonify

from app.libs.redprint import Redprint
from app.models.theme import Theme
from app.serializer.theme import ThemeItemSchema

api = Redprint('theme')


@api.route('', methods=['GET'])
def read_all_theme():
    themes = Theme.query.all()
    if themes is not None:
        theme_schema = ThemeItemSchema(many=True)
        result = theme_schema.dump(themes).data

        return jsonify(result)
    else:
        return jsonify({})
