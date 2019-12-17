import json
from django.db import models
from django.core.serializers import serialize
from django.contrib.auth.models import User


def uploadImage(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdatesQuerySet(models.QuerySet):

    def serialize(self):
        list_values = list(self.values("user", "content", "image", "id"))
        return json.dumps(list_values)


class UpdatesManager(models.Manager):

    def get_queryset(self):
        return UpdatesQuerySet(self.model, using=self._db)


class Updates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to=uploadImage, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UpdatesManager()

    def __str__(self):
        return self.content or ""


    def serialize(self):
        data = {
            "id": self.id,
            "user": self.user.id,
            "content": self.content,
            "image": str(self.image)
        }
        json_data = data
        return json.dumps(json_data)
