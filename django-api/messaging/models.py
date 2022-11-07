from django.db import models
from profiles.models import Profile


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(
        Profile, related_name="sender", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Profile, related_name="receiver", on_delete=models.CASCADE
    )
    image_url = models.CharField(
        max_length=255,
        default="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
    )
    message_body = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ["time"]

    def __str__(self):
        return self.sender
 