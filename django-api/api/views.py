"""User API views"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    # TODO: import and use correct serializier
    # serializer_class =


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token"""

    # TODO: import and use correct serializier
    # serializer_class =
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
