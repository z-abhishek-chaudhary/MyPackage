from ..models.All import Shops, Items

    

def get_shop(shop_id=None):
    # if shop_id is not None: 
    #     result = Shops.query.filterby(shop_id=shop_id).as_dict()
    #     return result
    # result = [s.as_dict() for s in Shops.query.all()]
    # return result

    if (shop_id is None):
        for i in Shops.query.all():
            print(i.shop_name, i.shop_description)
        return Shops.query.all()
    else:
        return Shops.query.filterby(shop_id=shop_id)



def get_item(item_id=None):
    # if item_id is not None: 
    #     result = Items.query.filterby(shop_id=item_id).as_dict()
    #     return result
    # result = [s.as_dict() for s in Items.query.all()]
    # return result

    if (item_id is None):
        for i in Items.query.all():
            print(i.item_name, i.item_description)
        return Items.query.all()
    else:
        return Items.query.filterby(item_id=item_id)
