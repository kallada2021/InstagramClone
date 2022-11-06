from django.test import TestCase # noqa
from django.urls import reverse 
from messaging.models import Message 
from messaging.serializers import MessageSerializer
from django.contrib.auth import get_user_model
from profiles.models import Profile
from rest_framework import status
from rest_framework.test import APIClient

MESSAGES_URL = reverse("messaging:messages-list")
# Create your tests here.

def detail_url(message_id):
    """Create and return a tag detail URL"""
    return reverse("messaging:message-detail", args=[message_id])

def create_user(**params):
    """Create and return a test user"""
    return get_user_model().objects.create_user(**params)

def create_message(**params):
    """Create and return sample recipe"""
    defaults = {
        "message_body": "Message Body",
    }

    defaults.update(params)  # overrides default values with params

    message = Message.objects.create(**defaults)
    return message

class PublicMessagesApiTests(TestCase):
    """Message API public endpoints tests"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint"""
        res = self.client.get(MESSAGES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)