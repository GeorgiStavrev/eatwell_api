from eatwell_api.auth.views import LoginView, RegisterView, BASE_ROUTE
from aiohttp import web


def register_routes(app):
    app.router.add_routes([
        web.post(BASE_ROUTE + "/login", LoginView),
        web.post(BASE_ROUTE + "/register", RegisterView)])
