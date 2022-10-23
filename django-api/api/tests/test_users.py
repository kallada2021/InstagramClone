"""Test for the User API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("api:create")


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
        payload: dict = {"username": "Test"}  # TODO: fill out payload dict
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(username=payload[""])  # TODO: Add key
        self.assertTrue(user.check_password(payload[""]))  # TODO: Add key

        # TODO: assert password is not in res.data that is returned

    def test_user_with_email_exists_error(self):
        """Test error returned if email already exists"""
        payload: dict = {}  # TODO create payload
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # TODO write test for duplicate username

    def test_password_too_short_error(self):
        """Test error returned if password is too short"""
        payload: dict = {}  # TODO: create payload

        res = None  # TODO: write post to url function
        # TODO: assert bad request returned
        user_exists: bool = get_user_model().objects.filter(email=payload["email"]).exists()
        # Check that user does not exist
