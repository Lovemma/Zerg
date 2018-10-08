# -*- coding: utf-8 -*-

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.mysql import TINYINT

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    status = Column(TINYINT, default=0)
    create_time = Column(DateTime,
                         default=datetime.utcnow)
    update_time = Column(DateTime,
                         default=datetime.utcnow,
                         onupdate=datetime.utcnow)


