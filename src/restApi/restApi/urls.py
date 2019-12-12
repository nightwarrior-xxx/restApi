from django.contrib import admin
from django.urls import path
from updates.views import (
    JsonCBV, JsonCBV2
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv', JsonCBV.as_view()),
    path('cbv2/', JsonCBV2.as_view()),
]
