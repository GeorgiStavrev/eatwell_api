from eatwell_api.models.models import Dish
from eatwell_api.base_view import BaseView

BASE_ROUTE = '/api/v1/dish'


class DishView(BaseView):
    def get_model(self):
        return Dish

    def get_base_route(self):
        return BASE_ROUTE

    def get_protected_routes(self):
        return self._protect_base_routes(BASE_ROUTE)

    def set_record_props_from_data(self, record, data):
        record.name = data['name']
        record.description = data['description']

    def record_to_dict(self, record):
        result = super(DishView, self).record_to_dict(record)
        result['name'] = record.name
        result['description'] = record.description

        return result
