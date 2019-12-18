from django.contrib import admin
from .models import StatusModel
from .forms import StatusModelForm

class StatusModelFormAdmin(admin.ModelAdmin):
    list_display = ["user", "__str__", "image"]
    form = StatusModelForm


admin.site.register(StatusModel, StatusModelFormAdmin)
