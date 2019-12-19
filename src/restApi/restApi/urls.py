from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from updates.views import (
    JsonCBV, JsonCBV2,
    SerializedListView,
    SerializedDetailView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/jwt/', obtain_jwt_token, name="jwtToken"),
    path('api/auth/jwt/refresh/', refresh_jwt_token, name="jwtRefreshToken"),
    path('api/updates/', include("updates.api.urls", namespace="updatesApi")),
    path('api/status/', include("status.api.urls", namespace="statusApi")),
]
