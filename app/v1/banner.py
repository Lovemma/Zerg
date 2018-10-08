# -*- coding: utf-8 -*-

from flask import abort, request, jsonify

from app import db
from app.libs.exceptions import HTTPException
from app.models.banner import BannerItem
from app.models.image import Image
from app.serializer.banner import BannerItemSchema
from app.libs.redprint import Redprint

api = Redprint('banner')

@api.route('/<int:banner_id>', methods=['GET'])
def read_one(banner_id):
    banner_item = (BannerItem.query
                   .filter(BannerItem.id == banner_id)
                   .one_or_none())

    if banner_item is not None:
        banner_item_schema = BannerItemSchema()
        return jsonify(banner_item_schema.dump(banner_item).data)

    else:
        raise HTTPException(404, f'Banner not found for Id {banner_id}')

@api.route('', methods=['POST'])
def create():
    args = request.get_json()
    banner_item = BannerItem()
    banner_item.img_id = args.get('img_id')
    banner_item.keyword = args.get('keyword')
    banner_item.type = args.get('type')
    banner_item.banner_id = args.get('banner_id')
    db.session.add(banner_item)
    db.session.commit()
    return 'success'
