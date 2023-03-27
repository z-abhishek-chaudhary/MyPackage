from .BaseRoutes import getNewRoute
from ..services.Items import ItemServices, ShopByItemService

routes = getNewRoute("items")
routes.add_url_rule('/', view_func=ItemServices.as_view('items'), methods=['GET', 'POST'])

routes.add_url_rule('/shops', view_func=ShopByItemService.as_view('items_shops'), methods=['GET','POST'])