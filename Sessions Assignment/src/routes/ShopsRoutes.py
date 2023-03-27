from .BaseRoutes import getNewRoute
from ..services.Shops import ShopServices, ItemByShopService

routes = getNewRoute("shops")
routes.add_url_rule('/', view_func=ShopServices.as_view('shops'), methods=['GET', 'POST'])
routes.add_url_rule('/items', view_func=ItemByShopService.as_view('shops_item'), methods=['GET','POST'])