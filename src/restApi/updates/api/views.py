import json
from updates.models import Updates as UpdatesModel
from updates.forms import UpdatesModelForm
from django.views.generic import View
from django.http import HttpResponse
from restApi.mixins import HttpResponseMixins
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .mixins import CSRFExemptMixins

class UpdatesApiListView(HttpResponseMixins, CSRFExemptMixins, View):

    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdatesModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        form = UpdatesModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            json_data = obj.serialize()
            return self.render_to_response(json_data, status=201)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=400)

        json_data = json.dumps({
            "message": "Something went wrong please try again"
        })
        return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({
            "message": "This is a put request. You are not allowed"
        })
        return self.render_to_response(json_data, status=403)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({
            "message": "This is a delete request. You cannot delete this List"
        })
        return self.render_to_response(json_data, status=403)


class UpdatesApiDetailView(HttpResponseMixins, CSRFExemptMixins, View):

    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdatesModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({
            "message": "This method is not allowed. Use /api/updates/ method."
        })
        return self.render_to_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({
            "message": "This is a put request. You are not allowed"
        })
        return self.render_to_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({
            "message": "This is a delete request. You cannot delete this entity"
        })
        return self.render_to_response(json_data, status=403)
