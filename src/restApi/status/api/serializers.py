from rest_framework import serializers
from status.models import StatusModel


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusModel
        fields = [
            "user",
            "content",
            "image"
        ]
