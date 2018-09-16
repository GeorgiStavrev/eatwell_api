from eatwell_api.menu.views import MenuView


def register_routes(app):
    app.router.add_route('*', '/menu/', MenuView)
