from eatwell_api.dish.views import DishView, BASE_ROUTE
from aiohttp import web


def register_routes(app):
    by_id_route = BASE_ROUTE + "/{id}"
    app.router.add_routes([web.get(BASE_ROUTE, DishView),
                           web.post(BASE_ROUTE, DishView),
                           web.get(by_id_route, DishView),
                           web.put(by_id_route, DishView),
                           web.delete(by_id_route, DishView)])
