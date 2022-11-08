from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False, required=False)
    owner_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ["id", "owner", "owner_id", "title", "body", "created_at", "updated_at"]
        # read_only_fields = ["id"]

    def create(self, **validated_data):
        """Create a Post"""
        auth_user = self.context["request"].user
        profile = Profile.objects.get(username=auth_user.username)

        post = Post.objects.create(profile, **validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source="posts.post.title")
    owner = serializers.ReadOnlyField(source="profiles.profile.username")

    class Meta:
        model = Comment
        fields = ["id", "owner", "post", "body", "created_at", "updated_at"]
        # read_only_fields = ["id", "owner", "post"]


class UpdateDeleteCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "owner", "post", "body", "created_at", "updated_at"]
