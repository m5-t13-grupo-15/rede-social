from rest_framework import serializers
from .models import Friends


class FriendListSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField(read_only=True)

    def get_friends(self, obj):
        return [
            dict(id=user.id, username=user.username, email=user.email)
            for user in obj.friends.all()
        ]

    class Meta:
        model = Friends
        fields = "__all__"
