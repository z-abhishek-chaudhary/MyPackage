from flask.views import MethodView
from flask import request
import json
from ..Common import get_item, get_item_shop


class ItemServices(MethodView):
    def __init__(self):
        self.id = None
    def get(self, *args, **kwargs):
        result = get_item()
        if result is not None:
            result = {
                "code": 200,
                "success": True,
                "result": result
            }
        else:
            result = {
                "code": 404,
                "success": False,
                "result": result
            }
        return result
    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = get_item(params['item_id'])

        if result is None:
            result = {
                "code": 404,
                "success": False,
                "result": result
            }
        else:
            result = {
                "code": 200,
                "success": True,
                "result": result
            }

        return result

class ShopByItemService(MethodView):

    def get(self, *args, **kwargs):
        result = get_item_shop()
        if result is not None:
            result = {
                "code": 200,
                "success": True,
                "result": result
            }
        else:
            result = {
                "code": 404,
                "success": False,
                "result": result
            }

        return result
    
    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = get_item_shop(params['item_id'])

        if result is None:
            result = {
                "code": 404,
                "success": False,
                "result": result
            }
        else:
            result = {
                "code": 200,
                "success": True,
                "result": result
            }
        return result