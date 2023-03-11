from rest_framework import serializers
from friends.models import FriendList
from followers.models import FollowersList
from .models import User
from friends.models import FriendList


class UserSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)

    def get_friends(self, obj):
        friends_list = FriendList.objects.get(owner=obj)
        friends = friends_list.friends.all()
        return friends

    def get_followers(self, obj):
        follower_list = FollowersList.objects.get(owner=obj)
        followers = follower_list.followers.all()
        return followers

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
        ]

        read_only_fields = [
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}
