from rest_framework import serializers
from .models import BondRequest
from users.models import User


class RequestSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    receiver = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BondRequest
        fields = "__all__"
        read_only_fields = ["id", "sender", "receiver", "sent_at"]

    def get_sender(self, obj: BondRequest):
        return dict(
            id=obj.sender.id, first_name=obj.sender.first_name, email=obj.sender.email
        )

    def get_receiver(self, obj: BondRequest):
        return dict(
            id=obj.receiver.id,
            first_name=obj.receiver.first_name,
            email=obj.receiver.email,
        )

    def create(self, validated_data):
        return BondRequest.objects.create(**validated_data)
