from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import *

app_name = "api"

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="apischema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="apischema"), name="apidocs"),
    path("user/create/", CreateUserView.as_view(), name="create"),
    path("user/token/", CreateTokenView.as_view(), name="token"),
]
