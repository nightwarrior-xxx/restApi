from django.db import models
from django.contrib.auth.models import User


def uploadImageTo(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):

    pass


class StatusModelManager(models.Manager):

    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class StatusModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=uploadImageTo, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = StatusModelManager()

    def __str__(self):
        return self.content[:40]


    class Meta:
        verbose_name = "Status Model"
        verbose_name_plural = "Status Models"

    @property
    def owner(self):
        return self.user
