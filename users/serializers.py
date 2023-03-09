from rest_framework import serializers
from .models import User
from friends.models import Friends


class UserSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField(read_only=True)

    def get_friends(self, obj):
        return Friends.objects.filter(owner_id=obj)

    def create(self, validated_data) -> User:
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "created_at",
            "updated_at",
            "friends",
        ]

        read_only_fields = [
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}
