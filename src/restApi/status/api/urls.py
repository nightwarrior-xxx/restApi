from django.urls import path
from .views import (
    StatusApiView,
    StatusApiDetailView,
)

app_name = "statusApi"

urlpatterns = [
    path('', StatusApiView.as_view()),
    path('<int:pk>/', StatusApiDetailView.as_view(), name="detail"),
]
