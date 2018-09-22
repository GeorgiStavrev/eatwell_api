from aiohttp import web


async def request_logger_middleware(app, handler):
    async def middleware(request):
        print(request)
        try:
            response = await handler(request)
            return response
        except Exception as e:
            err_response = {
                "state": "error",
                "message": str(e)
            }
            response = web.json_response(err_response, status=500)
            return response
    return middleware
