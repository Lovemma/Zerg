# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource

from app.models.banner import BannerItem
from app.serializer.banner import BannerItemSchema


class BannerCollection(Resource):
    def get(self):
        banners = BannerItem.query.all()
        if banners is not None:
            banner_item_schema = BannerItemSchema(many=True)
            results = banner_item_schema.dump(banners).data
            return jsonify(results)
