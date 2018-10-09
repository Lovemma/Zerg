# -*- coding: utf-8 -*-

from app.serializer.image import ImageSchema
from . import ma


class ThemeItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'topic_img')

    topic_img = ma.Nested(ImageSchema)
