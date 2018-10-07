from aiohttp import web
from simple_settings import settings

from eatwell_api.healthcheck.routes import register_routes as register_heathcheck_routes
from eatwell_api.auth.routes import register_routes as register_auth_routes
from eatwell_api.dish.routes import register_routes as register_dish_routes
from eatwell_api.recipe.routes import register_routes as register_recipe_routes
from eatwell_api.shoppingList.routes import register_routes as register_shoppingList_routes
from eatwell_api.menu.routes import register_routes as register_menu_routes

from eatwell_api.middlewares.version import version_middleware
from eatwell_api.middlewares.request_logger import request_logger_middleware
from eatwell_api.middlewares.auth import auth_middleware

from mongoengine import connect
import datetime
from eatwell_api.models.models import Metadata


def build_app(loop=None):
    app = web.Application(loop=loop, middlewares=get_middlewares())
    app.state = dict()
    app.on_startup.append(load_plugins)
    app.on_startup.append(setup)
    app.on_cleanup.append(cleanup_plugins)
    register_routes(app)
    return app


def register_routes(app):
    register_heathcheck_routes(app)
    register_auth_routes(app)
    register_dish_routes(app)
    register_recipe_routes(app)
    register_shoppingList_routes(app)
    register_menu_routes(app)


def get_middlewares():
    return [version_middleware, request_logger_middleware, auth_middleware]


async def load_plugins(app):
    print('Loading plugins...')
    print('Loading plugins finished.')


async def cleanup_plugins(app):
    print('Cleaning up plugins...')
    print('Cleaning up finished.')


async def setup(app):
    setup_db(app)


def setup_db(app):
    try:
        connect(host=settings.MONGO_CONNSTR, db=settings.DBNAME)
        meta = Metadata()
        meta.info = "SERVER_STARTED"
        meta.save()
        app.state['db'] = "CONNECTED"
    except Exception as e:
        app.state['db'] = "ERROR CONNECTING: " + str(e)
