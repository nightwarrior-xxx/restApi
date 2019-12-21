from rest_framework import serializers

from django.contrib.auth.models import User
from status.models import StatusModel

from status.api.serializers import StatusInLineUserSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "uri",
            "status"
        ]

    def get_uri(self, obj):
        return "/api/user/{id}".format(id=obj.id)

    def get_status(self, obj):
        request = self.context.get("request")
        qs = StatusModel.objects.filter(user=obj).order_by("-timestamp")
        status_limit = 10
        if request:
            status_limit = request.GET.get("limit")
            try:
                status_limit = int(status_limit)
            except:
                pass
        data = {
            "status_uri": self.get_uri(obj) + "/status/",
            "last_status": StatusInLineUserSerializer(qs.first()).data,
            "recent_list": StatusInLineUserSerializer(qs[:status_limit], many=True).data
        }
        return data
