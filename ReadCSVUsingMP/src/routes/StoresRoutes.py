from .BaseRoutes import getNewRoute
from ..services.Stores import StoresServices

routes = getNewRoute("stores")
routes.add_url_rule('/', view_func=StoresServices.as_view('store'), methods=['GET', 'POST'])