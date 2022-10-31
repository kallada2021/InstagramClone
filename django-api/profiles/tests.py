"""Test for the Profile API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Profile
from .serializers import ProfileDetailSerializer, ProfileSerializer

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
            username="testuser1",
            email="test12345@example.com",
            location="earth",
            gender="Male",
        )

        create_profile(
            username="testuser2",
            email="test12346@example.com",
            location="mars",
            gender="Female",
        )

        res = self.client.get(PROFILES_URL)

        profiles = Profile.objects.all().order_by("-created_at")
        serializer = ProfileSerializer(profiles, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_profile_detail_by_id(self):
        """Tests getting a profle by id"""
        profile = create_profile(
            username="testuser1",
            email="test123@example.com",
            location="earth",
            gender="Male",
        )
        url = detail_url(profile.id)

        res = self.client.get(url)
        serializer = ProfileDetailSerializer(profile)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_partial_update(self):
        """Test partial update of a profile."""
        original_location = "earth"
        profile = create_profile(
            firstname="Testy",
            location=original_location,
        )

        payload = {"firstname": "Tester"}
        url = detail_url(profile.id)

        res = self.client.patch(url, payload)
        profile.refresh_from_db()
        self.assertEqual(profile.firstname, payload["firstname"])
        self.assertEqual(profile.location, original_location)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_profile(self):
        """Test deleting a profile"""
        profile = create_profile(username="testuser1", email="test123@example.com")
        url = detail_url(profile.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    # TODO: write a test to check a user can not delete another user's profile
    def test_delete_profile_not_allowed(self):
        """Test deleting a profile not allowed"""
        # user = self.user
        # self.client.force_authenticate(user)
        user2 = get_user_model().objects.create_user(
            username="testuser2",
            email="test7890@example.com",
            password="testpass123",
        )
        profile = Profile.objects.get(username=user2.username)
        # profile = create_profile(username="testuser1", email="test12345@example.com")
        url = detail_url(profile.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Profile.objects.filter(username=user2.username).exists())
