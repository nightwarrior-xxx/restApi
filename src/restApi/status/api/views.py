from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from status.models import StatusModel
from status.api.serializers import StatusSerializer


class StatusListSearchApiView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        qs = StatusModel.objects.all()
        serialized = StatusSerializer(qs)
        return Response(serialized.data)

    def post(self, request, *args, **kwargs):
        qs = StatusModel.objects.all()
        serialized = StatusSerializer(qs)
        return Response(serialized.data)


# List and Search View
class StatusApiView(generics.ListAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        queryset = StatusModel.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(content__icontains=query)
        return queryset
