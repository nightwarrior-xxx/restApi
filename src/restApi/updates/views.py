from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from restApi.mixins import JsonMixinsResponse
from django.core.serializers import serialize
from updates.models import Updates

class JsonCBV(View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000
        }
        return JsonResponse(data, **kwargs)


class JsonCBV2(JsonMixinsResponse, View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):

    def get(self, request, *args, **kwargs):
        obj = Updates.objects.get(pk=1)
        data = obj.serialize()
        json_data = data
        return HttpResponse(json_data, content_type="application/json") 



class SerializedListView(View):

    def get(self, request, *args, **kwargs):
        qs = Updates.objects.all().serialize()
        json_data = qs
        return HttpResponse(json_data, content_type="application/json")
