"""Test for the Profile API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Profile

PROFILES_URL = reverse("profile:profile-list")


def detail_url(profile_id):
    """Create and return a detailed profile by ID URL"""
    return reverse("profile:profile-detail", args=[profile_id])


def create_profile(**params):
    """Create sample test profile"""
    defaults = {
        "firstname": "Test",
        "lastname": "User",
        "username": "testinguser",
        "email": "tester@example.com",
        "phone": "1234567890",
        "location": "Test Location",
        "aboutme": "Test About Me",
        "status": "available",
        "profile_image": "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
        "active": True,
        "age": 21,
        "gender": "Male",
    }

    defaults.update(params)
    profile = Profile.objects.create(**defaults)
    return profile


class PublicProfileApiTests(TestCase):
    """Profile API public endpoints tests"""

    def test_create_new_profile(self):
        """Tests creating a new profile based on model"""
        profile = create_profile()
        self.assertEqual(str(profile), f"{profile.firstname} {profile.lastname}")

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call get profile endpoint"""
        res = self.client.get(PROFILES_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProfilesAPITests(TestCase):
    """Test authenticated API requests"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="admin@example.com",
            password="testpass123",
        )
        self.client.force_authenticate(self.user)

    def test_create_user_profile(self):
        """Tests creating a profile post method"""
        payload: dict = {
            "username": "Testing123",
            "email": "testuser@example.com",
            "location": "earth",
            "gender": "Male",
        }

        res = self.client.post(PROFILES_URL, payload)
        print(f"profile res {res.data}")
        profile = Profile.objects.get(username=payload["username"])

        self.assertEqual(profile.username, payload["username"])
        self.assertEqual(profile.email, payload["email"])
        # Loops through all the payload values and compares to the db object
        for k, v in payload.items():
            self.assertEqual(getattr(profile, k), v)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_profiles(self):
        """Test getting a list of user profiles"""
        create_profile(
            {
                "username": "testuser1",
                "email": "test12345@example.com",
                "location": "earth",
                "gender": "Male",
            }
        )

        create_profile(
            {
                "username": "testuser2",
                "email": "test12346@example.com",
                "location": "mars",
                "gender": "Female",
            }
        )

        res = self.client.get(PROFILES_URL)

        recipes = Profile.objects.all().order_by("-created_at")
        # TODO serializer profiles (More than ONE!)
        # TODO assert 201 status and res data = serializer data

    def test_get_profile_detail_by_id(self):
        """Tests getting a profle by id"""
        profile = create_profile({})  # TODO pass in data
        url = detail_url()  # TODO pass profile id

        # TODO:  get URL response
        # Add and import DetailSerializer and assert serializer data == response data

    def test_partial_update(self):
        """Test partial update of a profile."""
        original_location = "earth"
        profile = create_profile(
            firstname="Testy",
            location=original_location,
        )

        payload = {"firstname": "Tester"}
        url = detail_url(profile.id)

        # TODO: call patch url with payload

        # TODO: assert status OK
        profile.refresh_from_db()
        # assert firstname changed and location did not change

    def test_delete_profile(self):
        """Test deleting a profile"""
        # TODO: create profile

        url = detail_url()
        res = self.client.delete(url)

        # TODO assert status code and check that profile does not exist

    # TODO: write a test to check a user can not delete another user's profile
