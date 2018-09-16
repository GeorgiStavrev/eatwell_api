from aiohttp import web

items = [
    {'name': "lamb mince", 'quantity': "750g/1lb 10½oz"},
    {'name': "onion, finely chopped", 'quantity': "1"},
    {'name': "garlic cloves, crushed", 'quantity': "2"},
    {'name': "dried oregano", 'quantity': "1 tsp"},
    {'name': "dried mint", 'quantity': "1½ tsp"},
    {'name': "bay leaf", 'quantity': "1"},
    {'name': "cinnamon", 'quantity': "1 stick"},
    {'name': "plain flour", 'quantity': "1 tbsp"},
    {'name': "tomato purée", 'quantity': "2 tbsp"},
    {'name': "aubergines, cut into 0.5cm slices", 'quantity': "2"},
    {
        'name': "Maris Piper potatoes, peeled and thinly sliced",
        'quantity': "500g/1lb 2oz"
    },
    {'name': "freshly ground black pepper"}
]


class ShoppingListView(web.View):
    async def get(self):
        return web.json_response(items)
