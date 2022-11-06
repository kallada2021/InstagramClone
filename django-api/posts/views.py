from profiles.models import Profile
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Maps Post Model to CRUD endpoints"""

    serializer_class = PostSerializer
    queryset = Post.objects.all()  # Model for the viewset
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """filters posts to user who created them"""
        user = self.request.user
        profile = Profile.objects.get(username=user.username)
        posts = self.queryset.filter(owner=profile).order_by("-created_at")
        return posts

    def perform_create(self, serializer):
        auth_user = self.request.user
        profile = Profile.objects.get(username=auth_user.username)
        serializer.save(owner=profile)


class CommentsView(generics.GenericAPIView):
    """Maps Comment Model to Put and Post endpoints"""

    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        try:
            id = self.kwargs.get("id")
            post = Post.objects.get(id=id)
        except:
            # TODO: Make generic using NotFound
            return Response({"message": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # request.data._mutable = True
        comment = request.data
        print(comment)
        print("Post ", post)
        user = request.user
        profile = Profile.objects.get(username=user.username)  # TODO add try and except for profile object

        Comment.objects.create(body=comment["body"], owner=profile, post=post)

        # serializer = self.serializer_class(data=comment)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(
            # serializer.data,
            {"message": "New Comment created", "body": comment["body"]},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request, **kwargs):
        try:
            id = self.kwargs.get("id")
            post = Post.objects.get(id=id)
        except:
            return Response({"message": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        try:
            comments = Comment.objects.filter(post_id=post.id)
        except:
            return Response({"message": "No comments found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(
            comments,
            many=True,
            context={"request": request},
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class CommentsUpdateDeleteView(generics.GenericAPIView):
    """Maps Comment Model to Patch, Put and Delete endpoints"""

    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, commentid):
        """Updates a comment"""
        try:
            comment = Comment.objects.get(id=commentid)
        except:
            return Response(
                {"message": "Comment not found."}, status=status.HTTP_404_NOT_FOUND
            )  # TODO: Make generic using NotFound

        data = request.data
        # TODO: update comment and return a response

    def delete():  # TODO: add parameters
        """Deletes a comment"""


# class CommentViewSet(
#     mixins.DestroyModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     viewsets.GenericViewSet,
# ):
#     """Maps Comment Model to CRUD endpoints"""

#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()  # Model for the viewset
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     # def get_queryset(self):
#     #     """filters comments to user who created them"""
#     #     user = self.request.user
#     #     profile = Profile.objects.get(username=user.username)
#     #     posts = self.queryset.filter(owner=profile).order_by("-created_at")
#     #     comments = self.queryset.filter(post=posts).order_by("-created_at")
#     #     return comments

#     # def perform_create(self, serializer):
#     #     auth_user = self.request.user
#     #     profile = Profile.objects.get(username=auth_user.username)
#     #     serializer.save(owner=profile)
