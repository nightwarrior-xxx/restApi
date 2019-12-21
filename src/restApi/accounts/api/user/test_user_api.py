from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth.models import User


class UserAPITest(APITestCase):
    """
    Ensure that user is registered successfully
    """

    def setUp(self):
        obj = User.objects.create(username="test", email="test@gmail.com")
        obj.set_password("test@123")
        obj.save()

    def test_created_user(self):
        qs = User.objects.filter(username="test")
        self.assertEqual(qs.count(), 1)

    def test_registered_user(self):
        url = reverse("accountsApi:apiRegister")
        data = {
            "username": "test5",
            "email": "test5@gmail.com",
            "password": "test5@123",
            "password2": "test5@123"
        }
        response = self.client.post(url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
