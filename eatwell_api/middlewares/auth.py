import jwt
from simple_settings import settings
from aiohttp import web
from eatwell_api.models.models import User


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, settings.JWT_SECRET,
                                     algorithms=[settings.JWT_ALGORITHM])
                request.user = User.objects.get(email=payload['email'])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                print("Failed to decode token.")
                request.user = None
                
        return await handler(request)
    return middleware
