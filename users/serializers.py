from rest_framework import serializers
from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
    extend_schema_field,
    inline_serializer,
)
from drf_spectacular.types import OpenApiTypes
from friends.models import FriendList
from followers.models import FollowersList
from followers.serializers import FollowersSerializer
from .models import User
from friends.models import FriendList
from friends.serializer import FriendListSerializer


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "friend list retrieve",
            summary="list friends",
            value={
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "username": "9mm5DLpCOUso2hmclNUlI7n6vxbfIMOEOj5vd_X5u4J5Qmw+xuu1cxSe_NgpYGgbF98KSJKlw9709eiFEINtZ",
                "email": "user@example.com",
                "created_at": "2023-03-12T23:19:12.639Z",
                "updated_at": "2023-03-12T23:19:12.639Z",
                "first_name": "string",
                "last_name": "string",
                "friends": [
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "username": "string",
                        "email": "user@example.com",
                    }
                ],
                "followers": [
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "username": "string",
                        "email": "user@example.com",
                    }
                ],
                "private": True,
            },
        )
    ]
)
class UserSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)

    @extend_schema_field(
        inline_serializer(
            name="user_friends",
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_friends(self, obj):
        friends_list = FriendList.objects.get(owner=obj)
        serializer = FriendListSerializer(friends_list)
        data = serializer.data["friends"]
        return data

    @extend_schema_field(
        inline_serializer(
            name="user_followers",
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_followers(self, obj):
        follower_list = FollowersList.objects.get(owner=obj)
        serializer = FollowersSerializer(follower_list)
        data = serializer.data["followers"]
        return data

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
            "friends",
            "followers",
            "private",
        ]

        read_only_fields = [
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}
