from rest_framework import serializers
from .models import Post, PostComments


class PostSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'public','comments']
        

class PostCommentsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    commented_at = serializers.CharField(read_only=True)
    comment_user = serializers.CharField(read_only=True)
    post = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        return PostComments.objects.create(**validated_data)
    
    class Meta:
        model = PostComments
        fields = ['id', 'post', 'comment_user', 'text', 'commented_at']
