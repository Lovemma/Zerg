# -*- coding: utf-8 -*-

from app.serializer import ma

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
