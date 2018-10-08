# -*- coding: utf-8 -*-
from app.serializer.image import ImageSchema
from . import ma


class BannerItemSchema(ma.Schema):
    class Meta:
        fields = ('keyword', 'img', 'type')

    img = ma.Nested(ImageSchema)
