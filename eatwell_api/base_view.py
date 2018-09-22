from aiohttp import web
import json
import datetime


class BaseView(web.View):

    def get_model(self):
        ...

    def get_base_route(self):
        ...

    def set_record_props_from_data(self, record, data):
        ...

    def record_to_dict(self, record):
        result = dict()
        result['id'] = str(record.id)
        result['last_modified'] = record.last_modified.__str__()
        return result

    async def get(self):
        object_id = self.request.match_info['id'] if 'id' in self.request.match_info else None
        if object_id:
            return await self.get_by_id(object_id)
        else:
            return await self.get_all()

    async def get_all(self):
        objects = self.get_model().objects
        results = {'data': [self.record_to_dict(ob)
                            for ob in objects], 'count': len(objects)}

        return web.json_response(results)

    async def get_by_id(self, id):
        obj = self._find_by_id(id)
        if obj:
            return web.json_response(self.record_to_dict(obj))
        else:
            return web.Response(text='Not Found', status=404)

    async def post(self):
        data = await self.request.json()

        new_ob = self.get_model()()
        self.set_record_props_from_data(new_ob, data)
        new_ob.save()

        headers = dict()
        headers['Location'] = self.get_base_route() + "/" + str(new_ob.id)
        return web.Response(status=201, headers=headers)

    async def put(self):
        object_id = self.request.match_info['id'] if 'id' in self.request.match_info else None
        obj = self._find_by_id(object_id)

        if obj:
            data = await self.request.json()
            self.set_record_props_from_data(obj, data)
            obj.last_modified = datetime.datetime.now
            obj.save()
            return web.Response(status=200)
        else:
            return web.Response(text="Not Found", status=404)

    async def delete(self):
        object_id = self.request.match_info['id'] if 'id' in self.request.match_info else None
        obj = self._find_by_id(object_id)

        if obj:
            obj.delete()
            return web.Response(status=200)
        else:
            return web.Response(text="Not Found", status=404)

    def _find_by_id(self, object_id):
        try:
            return self.get_model().objects.get(id=object_id) if object_id else None
        except:
            return None
