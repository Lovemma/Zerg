# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.models import Base

theme_product = Table(
    'theme_product', Base.metadata,
    Column('theme_id', Integer, ForeignKey('theme.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
)


class Theme(Base):
    __tablename__ = 'theme'

    name = Column(String(50), nullable=False)
    description = Column(String)
    topic_img_id = Column(Integer, ForeignKey('image.id'))
    head_img_id = Column(Integer, ForeignKey('image.id'))

    topic_img = relationship('Image', backref='theme_topic',
                             foreign_keys=[topic_img_id])
    head_img = relationship('Image', backref='theme_head',
                            foreign_keys=[head_img_id])

    products = relationship('Product', secondary=theme_product,
                            backref='themes')
