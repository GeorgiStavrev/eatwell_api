from eatwell_api.recipe.views import RecipeView, BASE_ROUTE
from aiohttp import web


def register_routes(app):
    by_id_route = BASE_ROUTE + "/{id}"
    app.router.add_routes([web.get(BASE_ROUTE, RecipeView),
                           web.post(BASE_ROUTE, RecipeView),
                           web.get(by_id_route, RecipeView),
                           web.put(by_id_route, RecipeView),
                           web.delete(by_id_route, RecipeView)])
