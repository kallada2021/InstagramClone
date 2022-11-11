from django.db.models import Q
from drf_spectacular.utils import (  # extend_schema_view,
    OpenApiParameter,
    OpenApiTypes,
    extend_schema,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile


# Extening swagger documentation to accept query parameters
@extend_schema(
    parameters=[
        OpenApiParameter(
            "username",
            OpenApiTypes.STR,
            description="Username of the profile to find",
        ),
    ]
)
@api_view(["GET"])
def getuserbyusername(request):
    username = request.query_params.get("username", None)
    users = Profile.objects.filter(Q(username=username)).values()
    payload = {
        "users": users,
    }
    return Response(payload, status=200)
