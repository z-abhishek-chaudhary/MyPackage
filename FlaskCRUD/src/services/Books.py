from ..common import get_books, add_book, update_book, delete_book
from flask import request
import json
from flask.views import MethodView

class BookService(MethodView):
    def __init__(self):
        self.id = None

    def get(self,*args, **kwargs):
        result = get_books()
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
    
    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = get_books(params['id'])
        
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

class BookAddService(MethodView):
    def get(self,*args, **kwargs):
        result = add_book()
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
    
    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = add_book(params)
        
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
    
class BookUpdateService(MethodView):
    def get(self, *args, **kwargs):
        result = update_book()
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

    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = update_book(params)
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

class BookDeleteService(MethodView):
    def get(self, *args, **kwargs):
        result = delete_book()
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

    def delete(self, *args, **kwargs):
        params = json.loads(request.data)
        result = delete_book(params['id'])
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