# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base


class Banner(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))



class BannerItem(Base):
    id = Column(Integer, primary_key=True)
    img_id = Column(Integer, nullable=False)
    key_word= Column(String(100), nullable=False)
    type = Column(SmallInteger, nullable=False, default=1)
    banner_id = Column(Integer, nullable=False)
