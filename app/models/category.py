# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer

from app.models import Base


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    topic_img_id = Column(Integer)
    description = Column(String(100))
