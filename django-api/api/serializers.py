"""Serializers for user API View"""
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers


# TODO: add fields for user model, check pw min length
class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""

    class Meta:
        model = get_user_model()
        fields = ["username"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for Auth Token"""

    def validate(self, attrs):
        """Validate and authenticate the user"""
        # TODO: add username
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
        )

        # TODO: check if not user and raise Validation Error
        msg = ""
        return attrs
