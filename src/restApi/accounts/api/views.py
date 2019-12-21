from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics

from rest_framework_jwt.settings import api_settings

from accounts.api.user.serializers import UserDetailSerializer

from .serializers import AccountSerializer
from .permission import AnonymousPermission

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class AuthAPIView(APIView):
    permission_classes = [AnonymousPermission]

    def post(self, request, *args, **kwargs):
        # print(request.user)
        if request.user.is_authenticated:
            return Response({"detail": "User is already authenticated"}, status=400)
        data = request.data
        username = data.get("username")
        password = data.get("password")
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        if qs.count() == 1:
            userObj = qs.first()
            if userObj.check_password(password):
                user = userObj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(
                    token, user, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"})


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    queryset = User.objects.all()
    permission_classes = [AnonymousPermission]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# class RegisterAPIView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         request.user
#         if request.user.is_authenticated:
#             return Response({"detail": "You is already registered"})
#         data = request.data
#         username = data.get("username")
#         email = data.get("email")
#         password = data.get("password")
#         password2 = data.get("password2")
#         if password != password2:
#             return Response({"password":"Both password does not match"})
#         qs = User.objects.filter(
#             Q(username__iexact=username)|
#             Q(email__iexact=email)
#         )
#         if qs.exists():
#             return Response({"detail": "User already exist"})
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token, user, request=request)
#             return Response(response)
