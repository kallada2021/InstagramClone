"""Database Models"""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


# TODO: add fields to user manager
class UserManager(BaseUserManager):
    """Manages users"""

    def create_user(self, email, username, password=None, **extras):
        """Create and Save a new user"""
        user = self.model(email=email, **extras)
        user.set_password(password)
        user.save(using=self._db)

        return user


# TODO: add fields to user model
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
