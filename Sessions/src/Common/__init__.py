from ..models.All import Shops, Items, Stocks
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..config.base_config import BaseConfig
import json

    

def get_shop(shop_id=None):
    if shop_id is not None: 
        result = [s.as_dict() for s in Shops.query.filter(Shops.shop_id==shop_id)]
        return result
    
    result = [s.as_dict() for s in Shops.query.all()]
    return result

    # if (shop_id is None):
    #     for i in Shops.query.all():
    #         print(i.shop_name, i.shop_description)
    #     return Shops.query.all()
    # else:
    #     return Shops.query.filterby(shop_id=shop_id)


def get_shop_item(shop_id=None):

        engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        if shop_id is not None:
            result = [s for s in session.query(Items.item_name, Items.item_description, Stocks.unit_count, Stocks.unit_price)
                .join(Stocks, Stocks.item_id == Items.item_id)
                .filter(Stocks.shop_id == shop_id)
                .all()]
            items_list = []
            for item in result:
                item_dict = {
                    'item_name': item[0],
                    'item_description': item[1],
                    'unit_count': item[2],
                    'unit_price': item[3]
                }
                items_list.append(item_dict)

            # convert the list of dictionaries to a JSON string
            items_json = json.dumps(items_list)

            # return the JSON string
            return json.loads(items_json)
        
        result = [s for s in session.query(Shops.shop_name, Items.item_name, Items.item_description, Stocks.unit_count, Stocks.unit_price).join(Stocks, Stocks.item_id == Items.item_id).all()]
        items_list = []
        for item in result:
            item_dict = {
                'shop_name': item[0],
                'item_name': item[1],
                'item_description': item[2],
                'unit_count': item[3],
                'unit_price': item[4]
            }
            items_list.append(item_dict)
        items_json = json.dumps(items_list)
        return json.loads(items_json) 
            
                       
    


def get_item(item_id=None):
    if item_id is not None: 
        result = [s.as_dict() for s in Items.query.filter(Items.item_id==item_id)]
        return result
    result = [s.as_dict() for s in Items.query.all()]
    return result


    # if (item_id is None):
    #     for i in Items.query.all():
    #         print(i.item_name, i.item_description)
    #     return Items.query.all()
    # else:
    #     return Items.query.filterby(item_id=item_id)


def get_item_shop(item_id=None):

        engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)
        session = Session()
        if item_id is not None:
            result = [s for s in session.query(Shops.shop_name, Shops.shop_description, Stocks.unit_count, Stocks.unit_price)
                .join(Stocks, Stocks.shop_id == Shops.shop_id)
                .filter(Stocks.item_id == item_id)
                .all()]
            items_list = []
            for item in result:
                item_dict = {
                    'shop_name': item[0],
                    'shop_description': item[1],
                    'unit_count': item[2],
                    'unit_price': item[3]
                }
                items_list.append(item_dict)

            # convert the list of dictionaries to a JSON string
            items_json = json.dumps(items_list)

            # return the JSON string
            return json.loads(items_json)
        
        result = [s for s in session.query(Items.item_name, Shops.shop_name, Shops.shop_description, Stocks.unit_count, Stocks.unit_price).join(Stocks, Stocks.shop_id == Shops.shop_id).all()]
        items_list = []
        for item in result:
            item_dict = {
                'item_name' : item[0],
                'shop_name': item[1],
                'shop_description': item[2],
                'unit_count': item[3],
                'unit_price': item[4]
            }
            items_list.append(item_dict)
        items_json = json.dumps(items_list)
        return json.loads(items_json)
        