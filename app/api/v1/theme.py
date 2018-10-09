# -*- coding: utf-8 -*-
from flask import jsonify

from app.libs.exceptions import NotFound
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


@api.route('/<int:theme_id>', methods=['GET'])
def read_one_theme(theme_id):
    theme = Theme.query.filter_by(id=theme_id).first()

    if theme is not None:
        theme_schema = ThemeItemSchema()
        result = theme_schema.dump(theme).data
        return jsonify(result)
    else:
        raise NotFound(f'Theme not found for Id {theme_id}')