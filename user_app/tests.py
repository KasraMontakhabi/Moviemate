from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
# Create your tests here.


class RegisterTestCase(APITestCase):

    def test_register(self):

        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "pass@123",
            "password2": "pass@123"
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testcase", password="pass@123")

    def test_login(self):

        data = {
            "username": "testcase",
            "password": "pass@123"
        }

        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        # fetch the token to my user
        self.token = Token.objects.get(user__username="testcase")
        # This means I am carrying my token.  loging in by using the token.
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
