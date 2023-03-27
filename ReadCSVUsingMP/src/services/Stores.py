from flask.views import MethodView
from flask import request
import json
from ..Common import get_product, put_data_in_db
import datetime


class StoresServices(MethodView):

    def get(self, *args, **kwargs):
        result = get_product()
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
        result = get_product(params['path'])
        
        if result is None:
            result = {
                "code": 404,
                "success": False,
                "result": result
            }
        else:
            start = datetime.datetime.now()
            put_data_in_db(result)
            end = datetime.datetime.now()
            print(end-start)
            result = {
                "code": 200,
                "success": True,
                "result": ["succes"]
            }
        return result