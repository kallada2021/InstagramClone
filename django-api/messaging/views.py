from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message


# Create your views here.
class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        return Response({"messages": messages}, status=200)
