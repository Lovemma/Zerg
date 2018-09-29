# -*- coding: utf-8 -*-

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer

db = SQLAlchemy(query_class=True)


class Base(db.Model):
    __abstract__ = True

    create_time = Column('create_time', Integer)
    delete_time = Column('delete_time', Integer)
    update_time = Column('update_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
