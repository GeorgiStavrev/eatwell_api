from aiohttp import web
from aiohttp_cors import CorsViewMixin


class HealthCheckView(web.View, CorsViewMixin):
    async def get(self):
        return web.json_response(self.request.app.state)
