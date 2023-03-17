from . import ShopsRoutes, ItemsRoutes, BaseRoutes

def init_app(app):
    app.register_blueprint(BaseRoutes.routes)
    app.register_blueprint(ShopsRoutes.routes)
    app.register_blueprint(ItemsRoutes.routes)
    return app
