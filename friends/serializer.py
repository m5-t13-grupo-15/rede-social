from rest_framework import serializers
from drf_spectacular.utils import (
    extend_schema_serializer,
    inline_serializer,
    extend_schema_field,
    OpenApiExample,
)
from .models import FriendList


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "friend list retrieve",
            summary="list friends",
            value={
                "owner": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "friends": [
                    {
                        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "username": "string",
                        "email": "user@example.com",
                    }
                ],
            },
        )
    ]
)
class FriendListSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField(read_only=True)

    @extend_schema_field(
        inline_serializer(
            name="friends",
            fields={
                "id": serializers.UUIDField(),
                "username": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_friends(self, obj):
        return [
            dict(id=user.id, username=user.username, email=user.email)
            for user in obj.friends.all()
        ]

    class Meta:
        model = FriendList
        fields = "__all__"
