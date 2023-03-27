from . import StoresRoutes, BaseRoutes

def init_app(app):
    app.register_blueprint(BaseRoutes.routes)
    app.register_blueprint(StoresRoutes.routes)
    return app
