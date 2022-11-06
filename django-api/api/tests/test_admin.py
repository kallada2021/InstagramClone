"""Tests for Django Admin """
import email
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django Admin"""

    def setUp(self):
        """Create User and Client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="user1", email="test@test.com", password="testpass123"
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@example.com", username="admin", password="testpass123", firstname="Test User"
        )

    def test_users_list(self):
        """Test that users are listed"""
        url = reverse("admin:api_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.username)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test edit user page"""
        url = reverse("admin:api_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.username)
