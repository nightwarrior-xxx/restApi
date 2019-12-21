from django.urls import path, include
from .views import (
    UserDetailAPIView,
    UserStatusAPIView
)

app_name = "userApi"

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name="userView"),
    path('<str:username>/status/', UserStatusAPIView.as_view(), name="statusView"),
]
