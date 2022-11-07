"""Tests for Comment model and API"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from posts.models import Comment, Post
from posts.serializers import CommentSerializer, PostSerializer
from profiles.models import Profile
from rest_framework import status
from rest_framework.test import APIClient

# COMMENTS_URL = reverse("posts:comments")


def detail_url(post_id):
    """Create and return comments for a post"""
    return reverse("posts:comments", args=[post_id])


def delete_update_comment_url(post_id, comment_id):
    """Create and return comments for a post"""
    return reverse("posts:comment", args=[post_id, comment_id])


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

    def test_post_create_comment_on_non_existant_post(self):
        """Tests creating a comment on a non existant post"""
        user = create_user(
            username="testingcreatecommentsuser",
            email="commenttester@example.com",
            password="testpass123",
        )
        self.client.force_authenticate(user)
        payload: dict = {
            "body": "No post!",
        }

        url = detail_url(100)
        res = self.client.post(url, payload, format="json")
        print("Post comment res ", res.json)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_comment(self):
        """Tests deleting a comment"""
        user = create_user(
            username="testingdeletecommentsuser",
            email="commenttester@example.com",
            password="testpass123",
        )
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)
        post = Post.objects.create(owner=profile, title="Test Post", body="Test Body")
        comment = Comment.objects.create(post=post, owner=profile, body="Test Comment")
        url = delete_update_comment_url(post.id, comment.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_delete_comment_on_another_users_post(self):
        """Tests deleting a comment on another users post"""
        user1 = create_user(
            username="testingdeletecommentsuser1",
            email="commenttester1@example.com",
            password="testpass123",
        )
        profile1 = Profile.objects.get(username=user1.username)
        self.client.force_authenticate(user1)
        user2 = create_user(
            username="testingdeletecommentsuser2",
            email="commenttester2@example.com",
            password="testpass123",
        )
        profile2 = Profile.objects.get(username=user2.username)

        post = Post.objects.create(owner=profile2, title="Test Post", body="Test Body")
        comment = Comment.objects.create(post=post, owner=profile2, body="Test Comment")
        url = delete_update_comment_url(post.id, comment.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Comment.objects.filter(id=comment.id).exists())

    def test_update_comment(self):
        """Tests updating a comment"""
        user = create_user(
            username="testingupdatecommentsuser",
            email="testcommenter@example.com",
            password="testpass123",
        )
        profile = Profile.objects.get(username=user.username)
        self.client.force_authenticate(user)
        post = Post.objects.create(owner=profile, title="Test Post", body="Test Body")
        comment = Comment.objects.create(post=post, owner=profile, body="Test Comment")
        payload = {"body": "Updated comment"}
        url = delete_update_comment_url(post.id, comment.id)
        res = self.client.put(url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["body"], "Updated comment")

    def test_update_comment_on_another_users_post(self):
        """Tests updating a comment on another users post"""
        user1 = create_user(
            username="testingupdatecommentsuser1",
            email="testcommenter1@example.com",
            password="testpass123",
        )
        profile1 = Profile.objects.get(username=user1.username)
        self.client.force_authenticate(user1)
        user2 = create_user(
            username="testingupdatecommentsuser2",
            email="testcommenter2@example.com",
            password="testpass123",
        )
        profile2 = Profile.objects.get(username=user2.username)
        post = Post.objects.create(owner=profile2, title="Test Post", body="Test Body")
        comment = Comment.objects.create(post=post, owner=profile2, body="Test Comment")
        payload = {"body": "Updated comment"}
        url = delete_update_comment_url(post.id, comment.id)
        res = self.client.put(url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Comment.objects.filter(id=comment.id).exists())
