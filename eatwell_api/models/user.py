from mongoengine import Document, StringField, DateTimeField
import datetime


class User(Document):
    email = StringField(required=True, max_length=40)
    hashed_password = StringField(required=True, max_length=512)
    salt = StringField(required=True, max_length=100)
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
    last_connection = DateTimeField(
        required=True, default=datetime.datetime.now)
