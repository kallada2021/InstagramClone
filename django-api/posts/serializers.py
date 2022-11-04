from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False, required=False)

    class Meta:
        model = Post
        fields = ["id", "owner", "title", "body", "created_at", "updated_at"]
        read_only_fields = ["id"]

    def create(self, **validated_data):
        """Create a Post"""
        auth_user = self.context["request"].user
        profile = Profile.objects.get(username=auth_user.username)

        post = Post.objects.create(profile, **validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=False, required=True)
    class Meta:
        model = Comment
        #fields = "__all__"
        fields = ["id", "post", "owner", "body", "created_at", "updated_at"]
        read_only_fields = ["id"]

    # TODO: get post by id
    def create(self, **validated_data):
        """Create a Comment"""
        auth_user = self.context["request"].user
        profile = Profile.objects.get(username=auth_user.username)
        post = Post.objects.get(id=validated_data["post"]["id"])    
        comment = Comment.objects.create(owner=profile,post=post,**validated_data)
        return comment
