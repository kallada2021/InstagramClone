from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsUpdateDeleteView, CommentsView, PostViewSet, get_all_posts

app_name = "posts"


router = DefaultRouter()
router.register("posts", PostViewSet)
# router.register("comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("all-posts/", get_all_posts),
    path("comment/<int:id>/", CommentsView.as_view(), name="comments"),
    path("comment/<int:id>/<int:commentid>", CommentsUpdateDeleteView.as_view(), name="comment"),
]
