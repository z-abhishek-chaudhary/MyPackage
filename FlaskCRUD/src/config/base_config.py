import os
from dotenv import load_dotenv

ROOT_DIR = os.path.join(os.path.dirname(__file__), "../..")
DOT_ENV_PATH = os.path.join(ROOT_DIR, ".env")
load_dotenv(DOT_ENV_PATH)


class BaseConfig(object):


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
    
    SQLALCHEMY_DATABASE_URI = getDBConnectionString()