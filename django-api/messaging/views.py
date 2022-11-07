from profiles.models import Profile
from rest_framework import generics, mixins, status, viewsets  # noqa
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response  # noqa

from .models import Message
from .serializers import MessageSerializer

# Create your views here.
# class MessageView(APIView):
#     def get(self, request):
#         messages = Message.objects.all()
#         return Response({"messages": messages}, status=200)


class MessageViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Maps Message Model to CRUD endpoints"""

    serializer_class = MessageSerializer
    queryset = Message.objects.all()  # Model for the viewset
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """filters messages to user who created them"""
        user = self.request.user
        profile = Profile.objects.get(username=user.username)
        messages = self.queryset.filter(sender=profile).order_by("-time")
        return messages

    def perform_create(self, serializer):
        auth_user = self.request.user
        profile = Profile.objects.get(username=auth_user.username)
        print("MessageSerializer",serializer.validated_data)
        serializer.save(sender=profile)

