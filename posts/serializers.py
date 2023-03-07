from rest_framework import serializers

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    public = serializers.BooleanField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
