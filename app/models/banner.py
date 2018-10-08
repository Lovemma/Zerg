# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import TINYINT

from app.models import Base


class Banner(Base):
    __tablename__ = 'banner'

    name = Column(String(50), comment='Banner名称，通常用作标示')
    description = Column(String(255), comment='Banner描述')


class BannerItem(Base):
    __tablename__ = 'banner_item'

    img_id = Column(Integer,
                    nullable=False,
                    comment='外键，关联image表')
    keyword = Column('key_word',
                     String(100),
                     nullable=False,
                     comment='执行关键字，根据不同的type含义不同')
    type = Column(TINYINT,
                  nullable=False,
                  default=1,
                  comment='跳转类型: 0)无 1)商品 2)专题')
    banner_id = Column(Integer,
                       nullable=False,
                       comment='外键，关联banner表')
