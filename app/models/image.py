# -*- coding: utf-8 -*-

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TINYINT

from app.models import Base


class Image(Base):
    __tablename__ = 'image'

    url = Column(String(255), comment='图片路径')
    origin = Column('from', TINYINT, default=1, comment='图片来源：1)本地 2)网络')

