import json
from src.services import Stores
import pandas as pd
from ..config.base_config import BaseConfig
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models.All import Shops
from multiprocessing import Pool, cpu_count
from functools import partial


def get_product(store_path = None):
    if store_path is None:
        return ["Please provide path"]
    return store_path


def process_data(row, db_uri):
    engine = create_engine(db_uri)
    factory = sessionmaker(bind=engine)
    session = factory()

    if row['country'] == 'india':
        new_rec = Shops(name=row['name'], description=row['desc'], country=row['country'])
        session.add(new_rec)
        session.commit()

    session.close()

def put_data_in_db(path):
    df = pd.read_csv(path,chunksize=20000)
    db_uri = BaseConfig.SQLALCHEMY_DATABASE_URI

    num_processes = cpu_count()
    chunk_size = len(df) // num_processes

    pool = Pool(num_processes)
    partial_process_data = partial(process_data, db_uri=db_uri)

    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size
        if i == num_processes - 1:
            end = len(df)
        pool.map(partial_process_data, df.iloc[start:end].to_dict('records'))

    pool.close()
    pool.join()





# def put_data_in_db(path):
#     df = pd.read_csv(path)
#     engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)
#     factory = sessionmaker(bind=engine)
#     session = factory()
        
#     for index, row in df.iterrows():
#         if(row['country']=="india"):
#             new_rec = Shops(name=row['name'], description=row['desc'], country=row['country'])
#             session.add(new_rec)
#             session.commit()

