from eatwell_api.models.dish import Dish
from eatwell_api.base_view import BaseView

BASE_ROUTE = '/api/v1/dish'


class DishView(BaseView):
    def get_model(self):
        return Dish

    def get_base_route(self):
        return BASE_ROUTE

    def set_record_props_from_data(self, record, data):
        record.name = data['name']
        record.description = data['description']

    def record_to_dict(self, record):
        result = super(DishView, self).record_to_dict(record)
        result['name'] = record.name
        result['description'] = record.description

        return result


# class DishView(web.View):
#     async def get(self):
#         dishes = Dish.objects
#         results = {'data': [self.dish_to_dict(ob)
#                             for ob in dishes], 'count': len(dishes)}

#         return web.json_response(results)

#     async def post(self):
#         data = await self.request.json()

#         new_dish = Dish()
#         new_dish.name = data['name']
#         new_dish.description = data['description']
#         new_dish.save()

#         headers = dict()
#         headers['Location'] = BASE_ROUTE + "/" + str(new_dish.id)
#         return web.Response(status=201, headers=headers)

#     async def delete(self):
#         dish_id = self.request.match_info['id']
#         try:
#             dish = Dish.objects.get(id=dish_id) if dish_id else None
#         except:
#             dish = None

#         if dish:
#             dish.delete()
#             return web.Response(status=200)
#         else:
#             return web.Response(text="Not Found", status=404)

#     def dish_to_dict(self, dish):
#         result = dict()
#         result['id'] = str(dish.id)
#         result['name'] = dish.name
#         result['description'] = dish.description

#         return result
