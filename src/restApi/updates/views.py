from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from restApi.mixins import JsonMixinsResponse


class JsonCBV(View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000
        }
        return JsonResponse(data)


class JsonCBV2(JsonMixinsResponse, View):

    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000
        }
        return self.render_to_json_response(data)

