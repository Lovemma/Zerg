# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from app.models import Base


class User(Base):

    id = Column(Integer, primary_key=True)
    openid = Column(String(50), nullable=False)
    nickname = Column(String(50))
    extend = Column(String(255))

