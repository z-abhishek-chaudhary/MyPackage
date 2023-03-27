from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import os
from models.All import Shops, Items


ROOT_DIR = os.path.join(os.path.dirname(__file__), ".")
DOT_ENV_PATH = os.path.join(ROOT_DIR, ".env")
load_dotenv(DOT_ENV_PATH)


def getDBConnectionString():
    config = {
        "app_settings": os.getenv('APP_SETTINGS'),
        "database": os.getenv('DATABASE'),
        "username": os.getenv('DB_USERNAME'),
        "host": os.getenv('DB_HOST'),
        "password": os.getenv('DB_PASSWORD'),
        "port": os.getenv('DB_PORT'),
    }

    con_string = f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

    return con_string


engine = create_engine(getDBConnectionString(), convert_unicode=True)
db_session = scoped_session(sessionmaker(autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    item = Items(id=1, name="Laptop", description="I am a laptop")
    db_session.add(item)
    shop = Shops(id=1, name="Bhupender", description="Hello!", item_id=1)
    db_session.add(shop)
    db_session.commit()

