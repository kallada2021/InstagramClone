from telnetlib import STATUS
from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    aboutme = models.TextField()
    status = models.CharField(max_length=255, default="unavailable")
    profile_image = models.CharField(max_length=255, default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profiles"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

