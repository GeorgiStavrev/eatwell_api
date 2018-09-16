from aiohttp import web
from simple_settings import settings

from eatwell_api.healthcheck.routes import register_routes as register_heathcheck_routes
from eatwell_api.dish.routes import register_routes as register_dish_routes
from eatwell_api.recipe.routes import register_routes as register_recipe_routes
from eatwell_api.shoppingList.routes import register_routes as register_shoppingList_routes
from eatwell_api.menu.routes import register_routes as register_menu_routes
from eatwell_api.middlewares.version import version_middleware


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())
    app.on_startup.append(load_plugins)
    app.on_cleanup.append(cleanup_plugins)
    register_routes(app)
    return app


def register_routes(app):
    register_heathcheck_routes(app)
    register_dish_routes(app)
    register_recipe_routes(app)
    register_shoppingList_routes(app)
    register_menu_routes(app)


def get_middlewares():
    return [version_middleware]


async def load_plugins(app):
    print('load_plugins')


async def cleanup_plugins(app):
    print('cleanup_plugins')
