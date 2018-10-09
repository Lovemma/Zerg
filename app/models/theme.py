# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models import Base
from app.models.image import Image


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
