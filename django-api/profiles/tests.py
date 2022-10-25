"""Test for the Profile API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Profile

PROFILES_URL = reverse("profiles:createprofile")  # Add Profile URL


def create_profile(**params):
    """Create sample test profile"""
    defaults = {
        # TODO: add all fields
        "firstname": "Test",
        "lastname": "User",
        "username": "testuser",
        "email": "test@example.com",
        "phone": "1234567890",
        "location": "Test Location",
        "aboutme": "Test About Me",
        "status": "available",
        "profile_image": "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
        "active": True,
        "age": 21,
        "gender":"Male",
    }

    defaults.update(params)
    profile = Profile.objects.create(**defaults)
    return profile


class ProfileApiTests(TestCase):
    """Profile API tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_profile(self):
        """Tests creating a profile"""
        payload: dict = {"username": "Test", "email": "test@example.com", "password": "Testp12"}
        profile = create_profile(payload)
        res = self.client.post(PROFILES_URL, payload)
        self.assertEqual(profile.username, payload["username"])
        self.assertEqual(profile.email, payload["email"])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # TODO: check fields exist self.assertEqual(str(profile), )
       
        

    def test_auth_required(self):
        """Test auth is required to get profiles"""
        # TODO: get profile url and assert unauthorized status code
        pass


class PrivateProfilesAPITests(TestCase):
    """Test authenticated API requests"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            # TODO add fields to create a test user
        )
        self.client.force_authenticate(self.user)

    def test_get_profiles(self):
        """Test getting a list of user profiles"""
        create_profile({})  # TODO pass in example paramas
        create_profile({})  # TODO pass in a second example params

        res = self.client.get(PROFILES_URL)

        recipes = Profile.objects.all().order_by("-created_at")
        # TODO serialize profiles (More than ONE!)
