from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_201_CREATED
class UserTesting(APITestCase):
    def setUp(self):
        User.objects.create_user(username="bitsbuild1",email="email1@email1.com",password="password")
    def test_create_user_success(self):
        data = {
            "username":"bitsbuild",
            "password":"password",
            "email":"email@email.com",
            "confirm_password":"password"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,HTTP_201_CREATED)
    def test_create_user_failure_passwords_not_matching(self):
        data = {
            "username":"bitsbuild",
            "password":"password",
            "confirm_password":"confirm_password",
            "email":"email@email.com"
        }
        response=self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
    def test_create_user_failure_username_exists(self):
        data = {
            "username":"bitsbuild1",
            "email":"email@email.com",
            "password":"password",
            "confirm_password":"password",
        }
        response=self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
    def test_create_user_failure_account_with_email_exists(self):
        data = {
            "username":"bitsbuild",
            "email":"email1@email1.com",
            "password":"password",
            "confirm_password":"password"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
    def test_create_user_failure_invalid_email_format(self):
        data = {
            "username":"bitsbuild",
            "email":"email",
            "password":"password",
            "confirm_password":"password"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
    def test_get_token_success(self):
        data = {
            "username":"bitsbuild1",
            "password":"password"
        }
        user = User.objects.filter(username="bitsbuild1").first()
        token= Token.objects.get(user=user)
        response = self.client.post(reverse('get-token'),data)
        self.assertEqual(response.data['token'],token.key)
    def test_get_token_failure(self):
        data = {
            "username":"bitsbuild1",
            "password":"password1"
        }
        response = self.client.post(reverse('get-token'),data)
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
    def test_delete_user_success(self):
        token = Token.objects.get(user__username="bitsbuild1")
        self.client.credentials(HTTP_AUTHORIZATION='Token '+str(token.key))
        response = self.client.delete(reverse('delete'))
        self.assertEqual(response.status_code,HTTP_200_OK)
    def test_delete_user_failure(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+'')
        response = self.client.delete(reverse('delete'))
        self.assertEqual(response.status_code,HTTP_401_UNAUTHORIZED)