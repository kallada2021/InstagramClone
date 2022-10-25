"""Database Models"""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """Manages users"""

    def create_user(self, email, username, password=None, **extras):
        """Create and Save a new user"""
        if not email:
            raise ValueError("User must have an email address.")
        elif not username:
            raise ValueError("User must have a username.")

        user = self.model(username=username, email=self.normalize_email(email), **extras)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates a superuser"""
        email = "admin@example.com"
        user = self.create_user(username=username, email=self.normalize_email(email))
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
