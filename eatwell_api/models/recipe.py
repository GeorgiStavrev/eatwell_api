from mongoengine import Document, StringField, DateTimeField, ListField
import datetime


class RecipeIngredient(Document):
    name = StringField(required=True, max_length=50)
    quantity = StringField(required=True, max_length=40)


class Recipe(Document):
    name = StringField(required=True, max_length=40)
    description = StringField(required=True, max_length=1000)
    video_url = StringField(required=True, max_length=512)
    tags = ListField(StringField(max_length=50))
    ingredients = ListField(RecipeIngredient())
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
