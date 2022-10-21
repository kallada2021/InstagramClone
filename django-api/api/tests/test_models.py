"""
Test for user models
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_successful(self):
        email = "test@example.com"
        password = "testpass123"
        username = "testuser123"
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_email_raises_error(self):
        """Test if user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(username="admin123", email="", password="test123")

    def test_new_user_without_username_raises_error(self):
        """Test if user without username raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(username="", email="test@example.com", password="test123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "admin123",
            "test@example.com",
            "test123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
