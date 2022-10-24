"""Test for the Profile API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from models import Profile


def create_user(**params):
    """Create and return a test user"""
    return get_user_model().objects.create_user(**params)


class ProfileApiTests(TestCase):
    """Profile API tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_profile(self):
        """Tests creating a profile"""
        profile = Profile.objects.create(
            # TODO: add all fields
        )

        # TODO: check fields exist self.assertEqual(str(profile), )
