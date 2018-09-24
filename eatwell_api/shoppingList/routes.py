from eatwell_api.shoppingList.views import ShoppingListView, BASE_ROUTE
from aiohttp import web


def register_routes(app):
    by_id_route = BASE_ROUTE + "/{id}"
    app.router.add_routes([web.get(BASE_ROUTE, ShoppingListView),
                           web.post(BASE_ROUTE, ShoppingListView),
                           web.get(by_id_route, ShoppingListView),
                           web.put(by_id_route, ShoppingListView),
                           web.delete(by_id_route, ShoppingListView)])
