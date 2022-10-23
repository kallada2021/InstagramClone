from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

app_name = "api"

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
    # path("user/create/", TODO: import view, name="create"),
    # TODO create token url
]
