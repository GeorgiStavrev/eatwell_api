from eatwell_api.dish.views import DishView


def register_routes(app):
    app.router.add_route('*', '/dish/', DishView)
