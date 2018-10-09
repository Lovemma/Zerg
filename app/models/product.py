# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import DECIMAL, TINYINT

from app.models import Base


class Product(Base):
    __tablename__ = 'product'

    name = Column(String(80), nullable=False)
    price = Column(DECIMAL(precision=6, scale=2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    main_img_url = Column(String)
    origin = Column('from', TINYINT, default=1)
    summary = Column(String(50))
    category_id = Column(Integer)
    img_id = Column(Integer)

