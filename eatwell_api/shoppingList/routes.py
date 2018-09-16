from eatwell_api.shoppingList.views import ShoppingListView


def register_routes(app):
    app.router.add_route('*', '/shoppingList/', ShoppingListView)
