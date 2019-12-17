from django.contrib import admin
from django.urls import path, include
from updates.views import (
    JsonCBV, JsonCBV2,
    SerializedListView,
    SerializedDetailView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/updates/', include("updates.api.urls", namespace="api")),
    # path('cbv/', JsonCBV.as_view()),
    # path('cbv2/', JsonCBV2.as_view()),
    # path('cbv/serialized/list', SerializedListView.as_view()),
    # path('cbv/serialized/detail', SerializedDetailView.as_view()),
]
