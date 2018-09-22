from aiohttp import web
from eatwell_api.models.user import User
import hashlib
import uuid
import re
import jwt

BASE_ROUTE = '/auth'
EMAIL_REGEX = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
SECRET = "DSAJKHGDASJKHASD"


class LoginView(web.View):
    async def post(self):
        try:
            data = await self.request.json()
            if 'email' in data:
                user = _find_user(data['email'])
                hashed_pass = _get_hash(data['password'], user.salt)
                if user and user.hashed_password == hashed_pass:
                    return _token_response(user)
                else:
                    return _unauthorized()
            else:
                return _unauthorized()
        except:
            return _unauthorized()


class RegisterView(web.View):
    async def post(self):
        try:
            data = await self.request.json()
            if 'email' in data and _validate_email(data['email']) and 'password' in data:
                if _find_user(data['email']):
                    return web.json_response({'error_code': 1, 'message': 'Already registers.'})

                salt = _get_salt()
                hashed_pass = _get_hash(data['password'], salt)

                new_user = User()
                new_user.email = data['email']
                new_user.salt = salt
                new_user.hashed_password = hashed_pass
                new_user.save()

                return _token_response(new_user)
            else:
                return web.Response(status=400, text='Bad request')
        except Exception as e:
            return web.Response(status=400, text='Bad request' + str(e))


def _find_user(email):
    try:
        return User.objects.get(email=email)
    except:
        return None


def _get_salt():
    return uuid.uuid4().hex


def _get_hash(password, salt):
    return hashlib.sha512((password + salt).encode()).hexdigest()


def _validate_email(email):
    match = re.match(EMAIL_REGEX, email)
    return match != None


def _unauthorized():
    return web.Response(status=401, text='Unauthorized')


def _token_response(user):
    encoded = jwt.encode({'email': user.email}, SECRET, algorithm='HS256')
    return web.json_response({'token': encoded.decode()})
