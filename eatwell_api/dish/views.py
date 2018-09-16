from aiohttp import web

dishes = [
    {
        '_id': '1',
        'name': 'Pad Thai',
        'permalink': 'pad-thai',
        'description':
        'Pad thai, or phad thai, is a stir-fried rice noodle dish commonly served as a street food and at most restaurants in Thailand.',
        'imgUrl':
        'https://res.cloudinary.com/hksqkdlah/image/upload/s--mZc--w8M--/c_scale,f_auto,h_688,q_jpegmini:2,w_688/32489_sfs-pad-thai-44'
    },
    {
        '_id': '2',
        'name': 'Mussaka',
        'permalink': 'mussaka',
        'description':
        'Moussaka is an eggplant- or potato-based dish, often including ground meat, in the Levant, Middle East, and Balkans, with many local and regional variations.',
        'imgUrl': 'https://karmelowy.pl/wp-content/uploads/2016/02/mussaka.jpg'
    }
]


class DishView(web.View):
    async def get(self):
        return web.json_response(dishes)
