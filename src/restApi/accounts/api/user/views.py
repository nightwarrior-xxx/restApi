from rest_framework import generics, permissions

from django.contrib.auth.models import User
from status.models import StatusModel

from .serializers import UserDetailSerializer
from status.api.serializers import StatusInLineUserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = "username"

    def get_serializer_context(self):
        return {"request": self.request}


class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInLineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return StatusModel.objects.none()
        return StatusModel.objects.filter(user__username=username)
