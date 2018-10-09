# -*- coding: utf-8 -*-

from flask import jsonify

from app.libs.exceptions import NotFound
from app.libs.redprint import Redprint
from app.models.banner import BannerItem
from app.serializer.banner import BannerItemSchema

api = Redprint('banner')


@api.route('', methods=['GET'])
def read_all():
    banners = BannerItem.query.all()
    if banners is not None:
        banner_item_schema = BannerItemSchema(many=True)
        results = banner_item_schema.dump(banners).data
        return jsonify(results)



@api.route('/<int:banner_id>', methods=['GET'])
def read_one(banner_id):
    banner_item = (BannerItem.query
                   .filter(BannerItem.id == banner_id)
                   .one_or_none())

    if banner_item is not None:
        banner_item_schema = BannerItemSchema()
        return jsonify(banner_item_schema.dump(banner_item).data)

    else:
        raise NotFound(msg=f'Banner not found for Id {banner_id}')
