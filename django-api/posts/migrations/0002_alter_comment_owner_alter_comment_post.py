# Generated by Django 4.1.2 on 2022-11-05 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="profiles.profile",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="posts.post",
            ),
        ),
    ]
