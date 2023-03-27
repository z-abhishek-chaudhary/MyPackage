from sqlalchemy import Column, String, text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, FLOAT

from . import db


Base = db.Model
meta_data = Base.metadata


class Shops(Base):
    __tablename__ = "products"
    id = Column(INTEGER(20), primary_key=True)
    name = Column(String(25))
    description = Column(String(200))
    country = Column(String(25))

    def as_dict(self):
        return {c.name : getattr(self,c.name) for c in self.__table__.columns}
    