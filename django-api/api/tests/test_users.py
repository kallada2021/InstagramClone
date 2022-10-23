"""Test for the User API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("api:create")
TOKEN_URL = reverse("api:token")


def create_user(**params):
    """Create and return a test user"""
    return get_user_model().objects.create_user(**params)


# TODO Make the test pass!
class PublicUserApiTests(TestCase):
    """Test public features of the user API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user"""
        payload: dict = {"username": "Test","email":"admin@example.com", "password":"Testp12"}
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(username=payload["username"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)


    def test_user_with_email_exists_error(self):
        """Test error returned if email already exists"""
        payload: dict = {"username": "Test","email":"admin@example.com", "password":"Testp12"}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_with_username_exists_error(self):
        """Test error returned if username already exists"""
        payload: dict = {"username": "Test","email":"admin@example.com", "password":"Testp12"}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short_error(self):
        """Test error returned if password is too short"""
        payload: dict = {"username": "Test","email":"admin@example.com", "passowrd":"Test"}
        res = self.client.post(CREATE_USER_URL,payload)
        user_exists: bool = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_token_for_user(self):
        """Test generates token for valid credentials"""
        user_details = {"username": "Testing", "password": "testuserpw", "email": "admin@example.com"}
        create_user(**user_details)
        payload: dict = {"username": user_details["username"], "password": user_details["password"], "email": user_details["email"]}
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_invalidcredentials_error(self):
        """Test error returned if invalid credentials"""
        user_details = {"username": "Testing","email":"admin@example.com", "password": "testuserpw"}
        create_user(**user_details)
        payload: dict = {"username": "Test","email":"admin@example.com", "password":"Testp12"}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nopassword_error(self):
        """Test error returned if no password"""
        user_details = {"username": "Testing","email":"admin@example.com", "password": "testuserpw"}
        create_user(**user_details)
        payload: dict = {"username": "Test","email":"admin@example.com", "password":""}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        