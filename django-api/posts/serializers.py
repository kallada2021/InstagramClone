from profiles.serializers import ProfileSerializer
from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id"]


class CommentSerializer(serializers.ModelSerializer):
    # TODO: add post field
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id"]
