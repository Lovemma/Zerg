# -*- coding: utf-8 -*-

from app.serializer.image import ImageSchema
from app.serializer.product import ProductRecentSchema
from . import ma


class ThemeItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'topic_img', 'head_img', 'products')

    topic_img = ma.Nested(ImageSchema)
    head_img = ma.Nested(ImageSchema)
    products = ma.Nested(ProductRecentSchema, many=True)
