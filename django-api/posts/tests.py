"""Tests for Posts model and API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from rest_framework.test import APIClient

from .models import Post


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


def create_post(user, **params):
    """Create and return sample recipe"""
    # TODO: fill in defaults
    defaults = {}

    defaults.update(params)  # overrides default values with params

    # TODO: create and return test post


class PublicPostsApiTests(TestCase):
    """Profile API public endpoints tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        """Tests creating a Post based on model"""
        profile = create_profile()
        post = Post.objects.create(
            owner=profile,
            title="Post Title",
            body="Post Body",
        )

        self.assertEqual(str(post), post.title)
