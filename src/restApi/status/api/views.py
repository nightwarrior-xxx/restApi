import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication

from status.models import StatusModel
from status.api.serializers import StatusSerializer

from django.shortcuts import get_object_or_404
from .utils import is_json


"""
Class Based views for Create and List + Update Delete and Retrieve.
"""


class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = StatusModel.objects.all()
        query = self.request.GET.get("q")
        # print(self.request.user)
        if query is not None:
            queryset = queryset.filter(content__icontains=query)
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatusApiDetailView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):

    # authentication_classes = []
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def detail(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
