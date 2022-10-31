from profiles.models import Profile
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import CommentSerializer, PostSerializer  # noqa


class PostViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """Maps Post Model to CRUD endpoints"""

    serializer_class = PostSerializer
    queryset = Post.objects.all()  # Model for the viewset
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """filters posts to user who created them"""
        user = self.request.user
        profile = Profile.objects.get(username=user.username)
        posts = self.queryset.filter(owner=profile).order_by("-created_at")
        return posts


# TODO create comments viewset class
