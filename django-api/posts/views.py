from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import CommentSerializer, PostSerializer  # noqa


class PostViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """Maps Post Model to CRUD endpoints"""

    serializer_class = PostSerializer
    queryset = Post.objects.all()  # Model for the viewset
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Get recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by("-created_at")


# TODO create comments viewset
