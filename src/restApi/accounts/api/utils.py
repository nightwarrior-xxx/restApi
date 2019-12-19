from django.utils import timezone
from django.conf import settings
# from restApi.rest_api_conf.main import JWT_AUTH

# abc = settings.JWT_AUTH

expiration_time = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': request.user.username,
        'expiration_time': timezone.now() +  expiration_time
    }
