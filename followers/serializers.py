from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field, inline_serializer
from .models import FollowersList


class FollowersSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField(read_only=True)

    @extend_schema_field(
        inline_serializer(
            name="followers",
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_followers(self, obj):
        return [
            dict(id=user.id, username=user.username, email=user.email)
            for user in obj.followers.all()
        ]

    class Meta:
        model = FollowersList
        fields = "__all__"
