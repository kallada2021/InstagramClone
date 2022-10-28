from django.shortcuts import render  # noqa
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Maps Profile Model to CRUD endpoints"""

    # TODO: Create Post View
