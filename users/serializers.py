from rest_framework import serializers
from friends.models import FriendList
from followers.models import FollowersList
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data) -> User:
        user = User.objects.create_user(**validated_data)
        FriendList.objects.create(owner=user)
        FollowersList.objects.create(owner=user)
        return user

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "created_at",
            "updated_at",
            "first_name",
            "last_name",
        ]

        read_only_fields = [
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}
