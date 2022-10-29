"""Tests for Comment model and API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa
from posts.models import Comment
from profiles.models import Profile
from rest_framework.test import APIClient


def create_user(**params):
    """Create and return a test user"""
    return get_user_model().objects.create_user(**params)


def create_profile(**params):
    """Create sample test profile"""
    defaults = {
        "firstname": "Test",
        "lastname": "User",
        "username": "testingpostsuser",
        "email": "poststester@example.com",
        "phone": "12345678910",
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


class PublicCommentsApiTests(TestCase):
    """Comments API public endpoints tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_comment(self):
        """Tests creating a Comment based on model"""
        # TODO: create test
