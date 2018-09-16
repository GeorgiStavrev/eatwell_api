from aiohttp import web

recipes = [
    {
        '_id': '1',
        'dishId': '1',
        'thumbnail': 'https://img.youtube.com/vi/m88rF0rwHo8/mqdefault.jpg',
        'videoUrl': 'https://www.youtube.com/embed/m88rF0rwHo8',
        'videoShown': False,
        'name': 'How to Make Classic Pad Thai | Cooking with Poo',
        'permalink': 'classic-pad-thai-cooking-with-poo',
        'description':
        'This is the description of the recipe. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus convallis mauris malesuada tempor facilisis. Curabitur erat velit, dapibus',
        'tags': 'foodtube',
        'ingredients': [
            {'name': 'pad thai or lo mein noodles', 'quantity': '8 ounces'},
            {'name': 'vegetable oil', 'quantity': '2 tablespoons'},
            {'name': 'garlic, minced', 'quantity': '1 clove'},
            {'name': 'eggs', 'quantity': '2 large '},
            {'name': 'soy sauce', 'quantity': '1 1/2 tablespoons'},
            {
                'name': 'fresh lime juice (from about 1 medium lime)',
                'quantity': '2 tablespoons'
            },
            {'name': 'brown sugar', 'quantity': '2 tablespoons'},
            {'name': 'fish sauce', 'quantity': '1 teaspoon'},
            {'name': 'red pepper flakes', 'quantity': '1/8 teaspoon'},
            {'name': 'green onions, sliced', 'quantity': '3'},
            {
                'name': 'fresh cilantro, leaves only, roughly chopped',
                'quantity': '1/4 bunch'
            },
            {'name': 'chopped, unsalted peanuts', 'quantity': '1/4 cup'}
        ]
    },
    {
        '_id': '2',
        'dishId': '1',
        'thumbnail': 'https://img.youtube.com/vi/F5-nfxQjfZU/mqdefault.jpg',
        'videoUrl': 'https://www.youtube.com/embed/F5-nfxQjfZU',
        'videoShown': False,
        'name': 'The BEST Pad Thai Recipe',
        'permalink': 'the-best-pad-thai-recipe',
        'tags': 'asianathome',
        'ingredients': [
            {'name': 'pad thai or lo mein noodles', 'quantity': '8 ounces'},
            {'name': 'vegetable oil', 'quantity': '2 tablespoons'},
            {'name': 'garlic, minced', 'quantity': '1 clove'},
            {'name': 'eggs', 'quantity': '2 large '},
            {'name': 'soy sauce', 'quantity': '1 1/2 tablespoons'},
            {
                'name': 'fresh lime juice (from about 1 medium lime)',
                'quantity': '2 tablespoons'
            },
            {'name': 'brown sugar', 'quantity': '2 tablespoons'},
            {'name': 'fish sauce', 'quantity': '1 teaspoon'},
            {'name': 'red pepper flakes', 'quantity': '1/8 teaspoon'},
            {'name': 'green onions, sliced', 'quantity': '3'},
            {
                'name': 'fresh cilantro, leaves only, roughly chopped',
                'quantity': '1/4 bunch'
            },
            {'name': 'chopped, unsalted peanuts', 'quantity': '1/4 cup'}
        ]
    },
    {
        '_id': '3',
        'dishId': '2',
        'name': 'Some moussaka recipe',
        'permalink': 'some-moussaka-recipe',
        'ingredients': [
            {'name': 'lamb mince', 'quantity': '750g/1lb 10½oz'},
            {'name': 'onion, finely chopped', 'quantity': '1'},
            {'name': 'garlic cloves, crushed', 'quantity': '2'},
            {'name': 'dried oregano', 'quantity': '1 tsp'},
            {'name': 'dried mint', 'quantity': '1½ tsp'},
            {'name': 'bay leaf', 'quantity': '1'},
            {'name': 'cinnamon', 'quantity': '1 stick'},
            {'name': 'plain flour', 'quantity': '1 tbsp'},
            {'name': 'red wine', 'quantity': '200ml/7fl oz'},
            {'name': 'tin chopped tomatoes', 'quantity': '400g'},
            {'name': 'tomato purée', 'quantity': '2 tbsp'},
            {'name': 'aubergines, cut into 0.5cm slices', 'quantity': '2'},
            {'name': 'fine sea salt, plus extra for seasoning', 'quantity': '1 tbsp'},
            {'name': 'olive oil', 'quantity': '100ml/3½fl oz'},
            {
                'name': 'Maris Piper potatoes, peeled and thinly sliced',
                'quantity': '500g/1lb 2oz'
            },
            {'name': 'freshly ground black pepper'}
        ]
    }
]


class RecipeView(web.View):
    async def get(self):
        return web.json_response(recipes)
