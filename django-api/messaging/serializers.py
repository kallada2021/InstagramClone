from profiles.serializers import ProfileSerializer
from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Serializes Message Model"""

    # id = serializers.IntegerField()
    sender_id = serializers.IntegerField(write_only=True)
    receiver_id = serializers.IntegerField(write_only=True)
    # sender = ProfileSerializer(many=False, required=False, read_only=True)
    # receiver = ProfileSerializer(many=False, required=False, read_only=True)

    class Meta:
        model = Message
        fields = [
            "id",
            # "sender",
            "sender_id",
            # "receiver",
            "receiver_id",
            "message_body",
            "time",
        ]

        read_only_fields = ["id"]
