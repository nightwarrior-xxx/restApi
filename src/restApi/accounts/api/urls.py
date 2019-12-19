from django.contrib import admin
from django.urls import path, include
from .views import (
    AuthAPIView,
    RegisterAPIView
)

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


app_name = "accountsApi"

urlpatterns = [
    path('', AuthAPIView.as_view(), name="authView"),
    path('register/', RegisterAPIView.as_view(), name="apiRegister"),
    path('jwt/', obtain_jwt_token, name="jwtToken"),
    path('jwt/refresh/', refresh_jwt_token, name="jwtRefreshToken")
]
