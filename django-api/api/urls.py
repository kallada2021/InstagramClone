from django.urls import include, path

from .views import CreateTokenView, CreateUserView, ManageUserView

app_name = "api"


urlpatterns = [
    path("user/create/", CreateUserView.as_view(), name="create"),
    path("user/token/", CreateTokenView.as_view(), name="token"),
    path("user/me/", ManageUserView.as_view(), name="me"),
    path("password-reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
]
