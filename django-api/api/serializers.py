"""Serializers for user API View"""
from django.contrib.auth import authenticate, get_user_model
from .models import User
from django.utils.translation import gettext as _
from rest_framework import serializers


# TODO: add fields for user model, check pw min length
class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password","firstname","lastname"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 7}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for Auth Token"""
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, attrs):
        """Validate and authenticate the user"""
        # TODO: add username
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials. Check username and password")
            raise serializers.ValidationError(msg, code="authentication")  
        attrs["user"] = user
        return attrs

#Change Password
class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if not self.context['request'].user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Wrong password."})
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()

