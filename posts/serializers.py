from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Post.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'public',]
