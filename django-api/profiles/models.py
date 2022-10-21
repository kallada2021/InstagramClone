from django.db import models


# Create your models here.
class Profile(models.Model):
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    aboutme = models.TextField()
    status = models.CharField(max_length=255, default="unavailable")
    profile_image = models.CharField(
        max_length=255, default="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y"
    )
    active = models.BooleanField(default=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(
        max_length=8,
        choices=GENDER,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profiles"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
