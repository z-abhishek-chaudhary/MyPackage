from sqlalchemy import Column, String, text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, FLOAT

from . import db


Base = db.Model
meta_data = Base.metadata


class Shops(Base):
    __tablename__ = "shops"
    shop_id = Column(INTEGER(20), primary_key=True)
    shop_name = Column(String(50))
    shop_description = Column(String(100))
    # item_id = Column(ForeignKey("items.item_id"), index=True)

    def as_dict(self):
        return {c.name : getattr(self,c.name) for c in self.__table__.columns}


class Items(Base):
    __tablename__ = "items"
    item_id = Column(INTEGER(20), primary_key=True)
    item_name = Column(String(50))
    item_description = Column(String(100))

    def as_dict(self):
        return {c.name : getattr(self, c.name) for c in self.__table__.columns}
    

class Stocks(Base):
    __tablename__ = "stocks"
    id = Column(INTEGER(20), primary_key=True, nullable=False)
    item_id = Column(INTEGER(20))
    shop_id = Column(INTEGER(20))
    unit_count = Column(INTEGER(50))
    unit_price = Column(FLOAT(50))
    
    def as_dict(self):
        return {c.name : getattr(self, c.name) for c in self.__table__.columns}
    