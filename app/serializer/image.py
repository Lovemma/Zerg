# -*- coding: utf-8 -*-

from . import ma

class ImageSchema(ma.Schema):

    class Meta:
        fields = ('url',)
