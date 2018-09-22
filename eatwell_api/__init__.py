import asyncio

from eatwell_api.factory import build_app


loop = asyncio.get_event_loop()
app = build_app(loop)
