from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProfilesViewSet, get_all_profiles

app_name = "profile"

router = DefaultRouter()
router.register("profiles", ProfilesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("all-profiles/", get_all_profiles, name="get-profiles"),
]
