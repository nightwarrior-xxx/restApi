from django.utils import timezone
from django.conf import settings
from rest_framework_jwt.settings import api_settings


expiration_time = api_settings.JWT_REFRESH_EXPIRATION_DELTA


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expiration_time': timezone.now() + expiration_time
    }
