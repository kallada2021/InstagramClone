from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MessageViewSet

app_name = "messaging"

router = DefaultRouter()
router.register("messages", MessageViewSet)

urlpatterns = [
   path("", include(router.urls)),
   
]
