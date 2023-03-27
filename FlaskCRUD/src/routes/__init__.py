from . import BaseRoutes, BookRoutes

def init_app(app):
    app.register_blueprint(BaseRoutes.routes)
    app.register_blueprint(BookRoutes.routes)
    return app