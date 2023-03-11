from rest_framework import serializers
from .models import FollowersList


class BondListSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField(read_only=True)

    def get_followers(self, obj):
        return [
            dict(id=user.id, username=user.username, email=user.email)
            for user in obj.followers.all()
        ]

    class Meta:
        model = FollowersList
        fields = "__all__"
