"""Tests for Posts model and API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from posts.models import Post
from posts.serializers import PostSerializer
from profiles.models import Profile
from rest_framework import status
from rest_framework.test import APIClient

POSTS_URL = reverse("posts:post-list")


def detail_url(post_id):
    """Create and return a tag detail URL"""
    return reverse("posts:post-detail", args=[post_id])


def create_user(**params):
    """Create and return a test user"""
    return get_user_model().objects.create_user(**params)


def create_profile(**params):
    """Create sample test profile"""
    defaults = {
        "firstname": "Test",
        "lastname": "User",
        "username": "testingpostsuser",
        "email": "poststester123@example.com",
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


def create_post(profile, **params):
    """Create and return sample recipe"""
    defaults = {
        "title": "Test Post",
        "body": "Test Body",
        "likes": 10,
    }

    defaults.update(params)  # overrides default values with params

    userpost = Post.objects.create(owner=profile, **defaults)
    return userpost


class PublicPostsApiTests(TestCase):
    """Profile API public endpoints tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        """Tests creating a Post based on model"""
        user = create_user(email="test013@example.com", password="testpass", username="testuser013")
        profile = Profile.objects.get(username=user.username)
        post = Post.objects.create(
            owner=profile,
            title="Post Title",
            body="Post Body",
        )

        self.assertEqual(str(post), post.title)


class PrivateTAgsAPITests(TestCase):
    """Test authenticated API requests"""

    def setUp(self) -> None:
        self.client = APIClient()
        # self.user = create_user(username="testingpostsuser", email="poststester@example.com")
        # self.client.force_authenticate(self.user)

    def test_get_posts(self):
        """Tests getting a list of posts"""
        user = create_user(username="testingpostsuser1", email="poststester1@example.com")
        profile = Profile.objects.get(id=user.id)

        self.client.force_authenticate(user)

        Post.objects.create(owner=profile, title="post title", body="post body")
        create_post(profile, title="title2", body="body1")

        res = self.client.get(POSTS_URL)
        posts = Post.objects.all().order_by("-id")
        serializer = PostSerializer(posts, many=True)

        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertEquals(res.data, serializer.data)

    def test_post_update(self):
        """Updating Post"""
        user = create_user(username="testingpostsuser2", email="poststester2@example.com")
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)
        post = Post.objects.create(owner=profile, title="My Day")
        payload = {"title": "Dessert Time!"}

        url = detail_url(post.id)
        res = self.client.patch(url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, payload["title"])

    def test_posts_limited_to_user(self):
        """Test list of posts is limited to authenticated user"""
        user = create_user(username="testingpostsuser2", email="poststester2@example.com")
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)

        user2 = create_user(username="other123", email="user2@example.com")
        profile2 = Profile.objects.get(username=user2.username)

        post = Post.objects.create(owner=profile, title="Test Post")
        Post.objects.create(owner=profile2, title="Test Day")

        res = self.client.get(POSTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["title"], post.title)
        self.assertEqual(res.data[0]["id"], post.id)

    def test_delete_post(self):
        """Test deleting a post."""
        user = create_user(username="testdeletepostsuser2", email="postdeletetester2@example.com")
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)
        post = Post.objects.create(owner=profile, title="I made Breakfast!", body="Yum Yum!")

        url = detail_url(post.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        posts = Post.objects.filter(title=post.title)
        self.assertFalse(posts.exists())
