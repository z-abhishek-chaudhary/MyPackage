from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from . import db

Base = db.Model

class BookShop(Base):
    __tablename__ = 'books'

    id = Column(INTEGER(20), primary_key=True, autoincrement=True)
    title = Column(String(50))
    author = Column(String(50))
    publish_year = Column(String(10))

    def as_dict(self):
        return {c.name : getattr(self,c.name) for c in self.__table__.columns}