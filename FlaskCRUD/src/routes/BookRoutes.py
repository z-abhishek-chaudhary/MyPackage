from .BaseRoutes import getNewRoute
from ..services.Books import BookService, BookAddService, BookUpdateService, BookDeleteService

routes = getNewRoute("books")
routes.add_url_rule('/', view_func=BookService.as_view('books'), methods=['GET', 'POST'])
routes.add_url_rule('/add', view_func=BookAddService.as_view('add'), methods=['GET', 'POST'])
routes.add_url_rule('/update', view_func=BookUpdateService.as_view('update'), methods=['GET', 'POST'])
routes.add_url_rule('/delete', view_func=BookDeleteService.as_view('delete'), methods=['GET','DELETE'])