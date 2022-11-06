"""Tests for Comment model and API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa
from posts.models import Comment, Post
from posts.serializers import CommentSerializer, PostSerializer
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from rest_framework import status
from rest_framework.test import APIClient

# COMMENTS_URL = reverse("posts:comments")


def detail_url(post_id):
    """Create and return comments for a post"""
    return reverse("posts:comments", args=[post_id])


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
        """Tests getting a Comment by url"""
        user = create_user(
            username="testingcommentsuser", email="commenttester012@example.com", password="testpass123"
        )
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
        url = detail_url(post.id)

        res = self.client.get(url)

        serializer = CommentSerializer(res.data, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(serializer.data), 2)
        self.assertEqual(comment.body, "Test Comment")
        self.assertEqual(comment2.body, "Testing Comment")

    def test_post_create_comment(self):
        """Tests creating a comment"""
        user = create_user(
            username="testingcreatecommentsuser", email="commentcraeatetester012@example.com", password="testpass123"
        )
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)
        post = Post.objects.create(
            owner=profile,
            title="Test Post",
            body="Test Body",
        )
        print("Profile id ", profile.id)
        print("Post id ", post.id)

        payload: dict = {
            "body": "Nice post!",
        }

        url = detail_url(post.id)

        res = self.client.post(url, payload, format="json")
        print("Post comment res ", res.json)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn(res.data["body"], "Nice post!")

    # TODO: test creating a comment on a non existant post, returns 404

    # TODO: create patch and delete comment test
