from django.urls import path, include

from .views import CreateTokenView, CreateUserView, ManageUserView

app_name = "api"

# TODO add reset password library and url REF: https://studygyaan.com/django/django-rest-framework-tutorial-change-password-and-reset-password
# Make migrations and migrate
urlpatterns = [
    path("user/create/", CreateUserView.as_view(), name="create"),
    path("user/token/", CreateTokenView.as_view(), name="token"),
    path("user/me/", ManageUserView.as_view(), name="me"),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
