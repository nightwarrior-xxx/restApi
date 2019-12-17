import json
from updates.models import Updates as UpdatesModel
from updates.forms import UpdatesModelForm
from django.views.generic import View
from django.http import HttpResponse
from restApi.mixins import HttpResponseMixins
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .mixins import CSRFExemptMixins
from .utils import is_json


class UpdatesApiListView(HttpResponseMixins, CSRFExemptMixins, View):

    is_json = True

    def get_queryset(self):
        qs = UpdatesModel.objects.all()
        self.queryset = qs
        return qs

    def get_object(self, id=None):

        if id is None:
            return None

        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get(self, request, *args, **kwargs):
        
        data = json.loads(request.body)
        passed_id = data.get("id", None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                json_data = json.dumps({"message": "Update not found !!!"})
                return self.render_to_response(json_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)

        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            json_data = json.dumps(
                {"message": "The entry is not in JSON format. Please enter valid JSON format."})
            return self.render_to_response(json_data, status=400)
        data = json.loads(request.body)
        print(data)
        form = UpdatesModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            json_data = obj.serialize()
            return self.render_to_response(json_data, status=202)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=404)

        json_data = json.dumps({
            "message": "Something went wrong please try again"
        })
        return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            json_data = json.dumps(
                {"message": "The entry is not in JSON format. Please enter valid JSON format."})
            return self.render_to_response(json_data, status=400)

        passed_data = json.loads(request.body)
        passed_id = passed_data.get("id")

        obj = self.get_object(id=passed_id)
        if obj is None:
            json_data = json.dumps({"message": "The entry does not exist"})
            return self.render_to_response(json_data, status=404)

        old_data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        if passed_id is None:
            json_data = json.dumps(
                {"id": "ID is a must required field to do this operation"})
            return self.render_to_response(json_data, status=400)

        for key, value in passed_data.items():
            old_data[key] = value

        form = UpdatesModelForm(old_data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            json_data = json.dumps(old_data)
            return self.render_to_response(json_data, status=201)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=400)

        json_data = json.dumps({"message": "Something is happening !!"})
        return self.render_to_response(json_data, status=404)

    def delete(self, request, *args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            json_data = json.dumps(
                {"message": "The entry is not in JSON format. Please enter valid JSON format."})
            return self.render_to_response(json_data, status=400)

        passed_data = json.loads(request.body)
        passed_id = passed_data.get("id", None)
        if passed_id is None:
            json_data = json.dumps(
                {"id": "ID is a must required field to do this operation"})
            return self.render_to_response(json_data, status=400)

        obj = self.get_object(id=passed_id)
        if obj is None:
            json_data = json.dumps({"message": "Please send the correct ID."})
            return self.render_to_response(json_data, status=404)

        deleted_obj, updates_stats = obj.delete()
        if deleted_obj is 1:
            json_data = json.dumps(
                {"message": "Entity with ID {id} deleted".format(id=id)})
            return self.render_to_response(json_data, status=200)

        json_data = json.dumps({
            "message": "This is a delete request, but something went wrong !!!"
        })
        return self.render_to_response(json_data, status=403)


class UpdatesApiDetailView(HttpResponseMixins, CSRFExemptMixins, View):

    is_json = True

    def get_object(self, id=None):
        qs = UpdatesModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            json_data = json.dumps({"message": "The entry does not exist"})
            return self.render_to_response(json_data, status=400)

        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, id, *args, **kwargs):
        json_data = json.dumps({
            "message": "This method is not allowed. Use /api/updates/ method."
        })
        return self.render_to_response(json_data, status=400)

    def put(self, request, id, *args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            json_data = json.dumps(
                {"message": "The entry is not in JSON format. Please enter valid JSON format."})
            return self.render_to_response(json_data, status=400)

        obj = self.get_object(id=id)
        if obj is None:
            json_data = json.dumps({"message": "The entry does not exist"})
            return self.render_to_response(json_data, status=404)

        old_data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)

        for key, value in passed_data.items():
            old_data[key] = value

        print(old_data, passed_data)

        form = UpdatesModelForm(old_data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            json_data = json.dumps(old_data)
            return self.render_to_response(json_data, status=201)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=400)

        json_data = json.dumps({"message": "Something is happening !!"})
        return self.render_to_response(json_data, status=404)

    def delete(self, request, id, *args, **kwargs):

        obj = self.get_object(id=id)
        if obj is None:
            json_data = json.dumps({"message": "Please send the correct ID."})
            return self.render_to_response(json_data, status=404)

        deleted_obj, updates_stats = obj.delete()
        if deleted_obj is 1:
            json_data = json.dumps(
                {"message": "Entity with ID {id} deleted".format(id=id)})
            return self.render_to_response(json_data, status=200)

        json_data = json.dumps({
            "message": "This is a delete request, but something went wrong !!!"
        })
        return self.render_to_response(json_data, status=403)
