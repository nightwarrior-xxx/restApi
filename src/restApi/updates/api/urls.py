from django.urls import path
from .views import (
    UpdatesApiListView,
    UpdatesApiDetailView
)

app_name = 'updatesApi'

urlpatterns = [
    path("", UpdatesApiListView.as_view(), name='apiUpdateList'),
    path("<int:id>/", UpdatesApiDetailView.as_view(), name="apiUpdateDetail"),
]
