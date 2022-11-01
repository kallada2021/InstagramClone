from profiles.models import Profile
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer  # noqa


class PostViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
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

    def perform_create(self, serializer):
        auth_user = self.request.user
        profile = Profile.objects.get(username=auth_user.username)
        serializer.save(owner=profile)


# TODO create comments viewset class

class CommentViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Maps Comment Model to CRUD endpoints"""

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()  # Model for the viewset
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """filters comments to user who created them"""
        user = self.request.user
        profile = Profile.objects.get(username=user.username)
        posts = self.queryset.filter(owner=profile).order_by("-created_at")
        comments = self.queryset.filter(post=posts).order_by("-created_at")
        return comments

    # def perform_create(self, serializer):
    #     auth_user = self.request.user
    #     profile = Profile.objects.get(username=auth_user.username)
    #     serializer.save(owner=profile)
