from eatwell_api.menu.views import MenuView, BASE_ROUTE
from aiohttp import web


def register_routes(app):
    by_id_route = BASE_ROUTE + "/{id}"
    app.router.add_routes([web.get(BASE_ROUTE, MenuView),
                           web.post(BASE_ROUTE, MenuView),
                           web.get(by_id_route, MenuView),
                           web.put(by_id_route, MenuView),
                           web.delete(by_id_route, MenuView)])
