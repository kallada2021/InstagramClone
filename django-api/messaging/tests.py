from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile  # noqa
from rest_framework import status
from rest_framework.test import APIClient

from messaging.models import Message
from messaging.serializers import MessageSerializer  # noqa

MESSAGES_URL = reverse("messaging:message-list")


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

    def test_create_message(self):
        """Test creating a new message"""
        user1 = create_user(email="messagingtester1@example.com", password="testpass", username="messagingtester1")
        profile1 = Profile.objects.get(username=user1.username)
        user2 = create_user(email="messagingtester2@example.com", password="testpass", username="messagingtester2")
        profile2 = Profile.objects.get(username=user2.username)
        message = create_message(sender=profile1, receiver=profile2, message_body="Test Message")
        self.assertEqual(message.message_body, "Test Message")


class PrivateMessagesApiTests(TestCase):
    """Message API private endpoints tests"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email="messagingtester123@example.com",
            password="testpass123",
            username="messagingtester123",
        )

    def test_retrieve_messages(self):
        """Test retrieving messages"""
        user1 = create_user(email="mesagingtester1@example.com", password="testpass", username="messagingtester1")
        profile1 = Profile.objects.get(username=user1.username)
        self.client.force_authenticate(user1)

        user2 = create_user(email="messagingtester2@example.com", password="testpass", username="messagingtester2")
        profile2 = Profile.objects.get(username=user2.username)

        message = create_message(sender=profile1, receiver=profile2, message_body="Test Message")
        res = self.client.get(MESSAGES_URL)

        message = Message.objects.all().order_by("-id")
        serializer = MessageSerializer(message, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

    def test_receiver_retrieve_messages(self):
        """Test receiver can retrieve messages"""
        user1 = create_user(email="mesagingtester1@example.com", password="testpass", username="messagingtester1")
        profile1 = Profile.objects.get(username=user1.username)

        user2 = create_user(email="messagingtester2@example.com", password="testpass", username="messagingtester2")
        profile2 = Profile.objects.get(username=user2.username)
        self.client.force_authenticate(user2)

        message = create_message(sender=profile1, receiver=profile2, message_body="Test Message")
        res = self.client.get(MESSAGES_URL)

        message = Message.objects.all().order_by("-id")
        serializer = MessageSerializer(message, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

    # TODO test other users can't see someone else message
    def test_other_user_get_message_error(self):
        """Tests that other users can't see other's messages"""
        pass

    def test_create_message(self):
        """Test creating a new message"""
        user1 = create_user(email="messagingtester3@example.com", password="testpass", username="messagingtester3")
        profile1 = Profile.objects.get(username=user1.username)
        self.client.force_authenticate(user1)

        user2 = create_user(email="messagingtester4@example.com", password="testpass", username="messagingtester4")
        profile2 = Profile.objects.get(username=user2.username)

        payload = {
            "sender_id": profile1.id,
            "receiver_id": profile2.id,
            "message_body": "Test Message",
        }
        res = self.client.post(MESSAGES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["message_body"], payload["message_body"])
        self.assertEqual(res.data["sender"]["username"], profile1.username)
