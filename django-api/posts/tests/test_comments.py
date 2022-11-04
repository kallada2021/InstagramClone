"""Tests for Comment model and API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa
from posts.models import Comment, Post
from profiles.models import Profile
from rest_framework.test import APIClient
from rest_framework import status
from posts.serializers import CommentSerializer

COMMENTS_URL = reverse("posts:comment-list")

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

    def create_profile():
        """Create sample test profile"""
        user = create_user(
            username="testingpostsuser",
            email="posttester456@example.com",
            password="testpass123",
        )
        profile = Profile.objects.get(username=user.username)
        
        return profile



    def test_create_comment(self):
        """Tests creating a Comment based on model"""
        profile = create_profile()
        post = Post.objects.create(
            owner=profile,
            title="Test Post",
            body="Test Body",
        )
        comment = Comment.objects.create(
            post=post,
            owner=profile,
            body="Test Comment",
        )
        self.assertEqual(comment.body, "Test Comment")



# TODO: create tests for private endpoints based on comments model
class PrivateCommentsApiTests(TestCase):
    """Comments API private endpoint tests"""
    
    def setUp(self) -> None:
        self.client = APIClient()


    def test_get_comment(self):
        """Tests creating a Comment based on model"""
        user = create_user(username="testingcommentsuser", email="commenttester012@example.com", password="testpass123")
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)
        post = Post.objects.create(
                owner=profile,
                title="Test Post",
                body="Test Body",
            )
        comment = Comment.objects.create(
                post=post,
                owner=profile,
                body="Test Comment",
            )
        comment2 = Comment.objects.create(
                post=post,
                owner=profile,
                body="Testing Comment",
            )
        res = self.client.get(COMMENTS_URL)
        serializer = CommentSerializer(res.data, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(comment.body, "Test Comment")
        self.assertEqual(comment2.body, "Testing Comment")
        #self.assertEqual(len(serializer.data), 2)