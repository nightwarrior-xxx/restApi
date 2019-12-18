from django.urls import path
from .views import (
    StatusApiView
)

app_name = "statusApi"

urlpatterns = [
    path('', StatusApiView.as_view(), name="list"),
    # path('create/', StatusApiCreateView.as_view(), name="create"),
    # path('<int>/', StatusApiDetailView.as_view(), name="detail"),
    # path('<int>/update', StatusApiUpdateView.as_view(), name="update"),
    # path('<int>/delete', StatusApiDeleteView.as_view(), name="delete"),
]
