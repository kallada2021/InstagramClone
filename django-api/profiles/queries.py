from django.http import HttpResponse
from .models import Profile
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def getuserbyusername(request):
  username = request.query_params.get('username', None)
  users = Profile.objects.filter(Q(username=username)).values()
  payload = {
    'users': users,
  }
  return Response(payload, status=200)