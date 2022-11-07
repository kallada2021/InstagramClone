from rest_framework import serializers
from profiles.serializers import ProfileSerializer
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Serializes Message Model"""
    sender = ProfileSerializer(many=False, required=False)
    receiver = ProfileSerializer(many=False, required=False)
    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "message_body", "time"]
