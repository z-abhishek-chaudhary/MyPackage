from .BaseRoutes import getNewRoute
from ..services.Shops import ShopServices

routes = getNewRoute("shops")
routes.add_url_rule('/', view_func=ShopServices.as_view('shops'), methods=['GET', 'POST'])

