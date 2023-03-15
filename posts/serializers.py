from rest_framework import serializers
from .models import Post, PostComments


class PostCommentsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    commented_at = serializers.CharField(read_only=True)
    comment_user = serializers.CharField(read_only=True)
    # post = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return PostComments.objects.create(**validated_data)

    class Meta:
        model = PostComments
        fields = ["id", "comment_user", "text", "commented_at"]


class PostSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    post_comments_user = PostCommentsSerializer(read_only=True, many=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Post
        fields = ["id", "user", "content", "public", "post_comments_user", "posted_at"]
