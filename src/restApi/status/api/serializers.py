from rest_framework import serializers
from status.models import StatusModel

from accounts.api.serializers import UserPublicSerializer


class StatusInLineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = StatusModel
        fields = [
            "uri",
            "id",
            "content",
            "image"
        ]

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = StatusModel
        fields = [
            "uri",
            "id",
            "user",
            "content",
            "image"
        ]
        read_only_fields = ['user']

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)
