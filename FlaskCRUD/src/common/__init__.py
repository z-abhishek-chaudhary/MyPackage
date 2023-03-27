from ..models.All import BookShop
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text, update
from ..config.base_config import BaseConfig
import json

engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def get_books(book_id=None):
    if book_id is None:
        return [s.as_dict() for s in BookShop.query.all()]
    else:
        return [s.as_dict() for s in BookShop.query.filter(BookShop.id==book_id)]
    

def add_book(new_book=None):
    if new_book is not None:
        session = Session()
        new_row = BookShop(title = new_book['title'], author = new_book['author'], publish_year = new_book['publish_year'])
        session.add(new_row)
        session.commit()
        session.close()
        return "New Book Added"
    else :
        return "Please Provide Valid Data"
    
def update_book(new_book=None):
    if new_book is not None:
        id = new_book['id']
        title = new_book['title']
        author = new_book['author']
        publish_year = new_book['publish_year']
        session = Session()

        book_upd = session.query(BookShop).filter_by(id=id).first()
        book_upd.title = title
        book_upd.author = author
        book_upd.publish_year = publish_year
        session.commit()

        session.close()

        return "Data update Successfully"
    
    else:
        return "Please prodive data to update"

def delete_book(book_id = None):
    if book_id is not None:
        session = Session()
        delete_row = session.query(BookShop).filter_by(id=book_id).first()
        session.delete(delete_row)
        session.commit()
        return "Book Deleted from the database"
    else:
        return "Unable to delete"