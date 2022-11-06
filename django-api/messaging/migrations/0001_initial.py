# Generated by Django 4.1.2 on 2022-11-05 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                (
                    "image_url",
                    models.CharField(
                        default="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
                        max_length=255,
                    ),
                ),
                ("message_body", models.CharField(max_length=100)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to="profiles.profile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="profiles.profile",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Messages",
                "ordering": ["time"],
            },
        ),
    ]
