from mongoengine import Document, StringField, DateTimeField, ListField, GenericReferenceField, ReferenceField, BooleanField
import datetime


class Metadata(Document):
    info = StringField(required=True, max_length=20)
    published = DateTimeField(default=datetime.datetime.now)


class User(Document):
    email = StringField(required=True, max_length=40)
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=100)
    hashed_password = StringField(required=True, max_length=512)
    salt = StringField(required=True, max_length=100)
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
    last_connection = DateTimeField(
        required=True, default=datetime.datetime.now)


class Dish(Document):
    name = StringField(required=True, max_length=40)
    description = StringField(required=True, max_length=1000)
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)


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


class Menu(Document):
    name = StringField(required=True, default="Menu", max_length=100)
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
    items = ListField(ReferenceField(Recipe))


class ListItem(Document):
    name = StringField(required=True, max_length=100)
    value = BooleanField(required=True, default=False)


class ShoppingList(Document):
    name = StringField(required=False, max_length=100)
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
    items = ListField(ListItem())


class Favorites(Document):
    items = ListField(GenericReferenceField())
    last_modified = DateTimeField(required=True, default=datetime.datetime.now)
