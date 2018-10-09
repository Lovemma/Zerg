# -*- coding: utf-8 -*-
from flask import request, url_for
from marshmallow import post_dump

from . import ma


class ImageSchema(ma.Schema):
    class Meta:
        fields = ('url',)

    @post_dump
    def get_url(self, item):
        url = item.get('url')
        base_api = request.host_url.rstrip('/')
        item['url'] = base_api + url_for('static', filename='images' + url)
        return item
