from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileDetailSerializer, ProfileSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    """Maps Profile Model to CRUD endpoints"""

    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileSerializer

        return self.serializer_class

    # def get_queryset(self):
    #     """Get profiles for authenticated user"""
    #     return self.queryset.filter(username=self.request.user.username).order_by("-created_at")
