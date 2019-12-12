from django.db import models
from django.contrib.auth.models import User


def uploadImage(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class Updates(models.Model):
    user        = models.ForeignKey(User, on_delete = models.CASCADE)
    content     = models.TextField()
    image       = models.ImageField(upload_to = uploadImage, blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.content or ""
