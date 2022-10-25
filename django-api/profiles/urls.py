from django.urls import path  # noqa

from .views import ProfilesViewSet  # noqa

app_name = "profiles"  
# TODO: add endpoint for profiles
urlpatterns = [path("profile/create", ProfilesViewSet.as_view(),name = "createprofile")]
