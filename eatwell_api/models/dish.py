from mongoengine import Document, StringField, DateTimeField
import datetime


class Dish(Document):
    name = StringField(required=True, max_length=40)
    description = StringField(required=True, max_length=1000)
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
