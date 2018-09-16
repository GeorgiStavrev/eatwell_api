from eatwell_api.recipe.views import RecipeView


def register_routes(app):
    app.router.add_route('*', '/recipe/', RecipeView)
