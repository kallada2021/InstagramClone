from django.urls import path
from .views import MessageView

app_name = 'messaging'

urlpatterns = [
    path('messages/', MessageView.as_view()),
]