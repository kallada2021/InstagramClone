from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "firstname",
            "lastname",
            "username",
            "email",
            "location",
            "profile_image",
            "id",
        ]
        read_only_fields = ["id"]


class ProfileDetailSerializer(ProfileSerializer):
    """Serializer to return a detailed profile"""

    class Meta(ProfileSerializer.Meta):
        fields = ProfileSerializer.Meta.fields + [
            "active",
            "age",
            "aboutme",
            "gender",
            "status",
        ]
