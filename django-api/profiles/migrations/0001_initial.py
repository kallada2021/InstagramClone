# Generated by Django 4.1.2 on 2022-11-05 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(blank=True, max_length=255)),
                ("lastname", models.CharField(blank=True, max_length=255)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=255)),
                ("location", models.CharField(blank=True, max_length=255)),
                ("aboutme", models.TextField(blank=True)),
                ("status", models.CharField(default="unavailable", max_length=255)),
                (
                    "profile_image",
                    models.CharField(
                        default="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
                        max_length=255,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("age", models.IntegerField(default=0)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=8
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Profiles",
                "ordering": ["-created_at"],
            },
        ),
    ]
