from .BaseRoutes import getNewRoute
from ..services.Items import ItemServices

routes = getNewRoute("items")
routes.add_url_rule('/', view_func=ItemServices.as_view('items'), methods=['GET', 'POST'])

