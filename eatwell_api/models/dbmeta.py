from mongoengine import Document, DateTimeField, StringField
import datetime


class Metadata(Document):
    info = StringField(required=True, max_length=20)
    published = DateTimeField(default=datetime.datetime.now)
