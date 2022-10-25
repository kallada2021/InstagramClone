from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Profile


class ProfilesViewSet(viewsets.ModelViewSet):
    """Maps Profile Model to CRUD endpoints"""

    # TODO: add and import serializer
    queryset = Profile.objects.all()
    # TODO: Add permissions and authentication class
