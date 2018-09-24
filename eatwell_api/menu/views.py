from aiohttp import web
from eatwell_api.base_view import BaseView
from eatwell_api.models.models import Menu

BASE_ROUTE = '/api/v1/menu'


class MenuView(BaseView):
    def get_model(self):
        return Menu

    def get_base_route(self):
        return BASE_ROUTE

    def get_protected_routes(self):
        return self._protect_base_routes(BASE_ROUTE)

    def set_record_props_from_data(self, record, data):
        record.name = data['name']

    def record_to_dict(self, record):
        result = super(MenuView, self).record_to_dict(record)
        result['name'] = record.name

        return result
