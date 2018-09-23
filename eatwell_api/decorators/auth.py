from aiohttp import web


def check_auth(func):
    async def wrapper(view):
        if _is_route_protected(view, view.request.match_info.route) and not view.request.user:
            return web.json_response({'message': 'Auth required'}, status=401)
        return await func(view)
    return wrapper


def _is_route_protected(view, route):
    protected = view.get_protected_routes()

    if '*' in protected and (protected['*'] == '*' or route.method in protected['*']):
        return True

    if route.resource.canonical in protected.keys():
        if route.method in protected[route.resource.canonical]:
            return True

    return False
