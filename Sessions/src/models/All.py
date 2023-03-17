from sqlalchemy import Column, String, text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

from . import db


Base = db.Model
meta_data = Base.metadata


class Shops(Base):
    __tablename__ = "shops"
    shop_id = Column(INTEGER(20), primary_key=True)
    shop_name = Column(String(50))
    shop_description = Column(String(100))
    item_id = Column(ForeignKey("items.item_id"), index=True)


class Items(Base):
    __tablename__ = "items"
    item_id = Column(INTEGER(20), primary_key=True)
    item_name = Column(String(50))
    item_description = Column(String(100))
