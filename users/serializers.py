from rest_framework import serializers
from .models import User
from friends.models import FriendList


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data) -> User:
        user = User.objects.create_user(**validated_data)
        FriendList.objects.create(owner=user)
        return user

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "created_at", "updated_at"]

        read_only_fields = [
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}
