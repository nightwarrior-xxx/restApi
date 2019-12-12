from django.contrib import admin
from .models import Updates

class UpdatesModelAdmin(admin.ModelAdmin):

    class Meta:
        fields = ('user', 'content', 'image', 'timestamp', 'updated')
        model = Updates


admin.site.register(Updates, UpdatesModelAdmin)
