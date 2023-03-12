from rest_framework import serializers
from drf_spectacular.utils import (
    extend_schema_serializer,
    OpenApiExample,
    extend_schema_field,
    inline_serializer,
)
from .models import BondRequest
from users.models import User


class BondFriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    receiver = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BondRequest
        fields = "__all__"
        read_only_fields = [
            "id",
            "sender",
            "receiver",
            "sent_at",
            "request_type",
            "aproved",
            "is_active",
        ]

    @extend_schema_field(
        inline_serializer(
            name="sender_friend",
            fields={
                "id": serializers.UUIDField(),
                "first_name": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_sender(self, obj: BondRequest):
        return dict(
            id=obj.sender.id, first_name=obj.sender.first_name, email=obj.sender.email
        )

    @extend_schema_field(
        inline_serializer(
            name="receiver_friend",
            fields={
                "id": serializers.UUIDField(),
                "first_name": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_receiver(self, obj: BondRequest):
        return dict(
            id=obj.receiver.id,
            first_name=obj.receiver.first_name,
            email=obj.receiver.email,
        )

    def create(self, validated_data):
        return BondRequest.objects.create(**validated_data)


class BondFollowerRequestSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    receiver = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BondRequest
        fields = "__all__"
        read_only_fields = [
            "id",
            "sender",
            "receiver",
            "sent_at",
            "request_type",
            "aproved",
            "is_active",
        ]

    @extend_schema_field(
        inline_serializer(
            name="sender_follower",
            fields={
                "id": serializers.UUIDField(),
                "first_name": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_sender(self, obj: BondRequest):
        return dict(
            id=obj.sender.id, first_name=obj.sender.first_name, email=obj.sender.email
        )

    @extend_schema_field(
        inline_serializer(
            name="receiver_follower",
            fields={
                "id": serializers.UUIDField(),
                "first_name": serializers.CharField(),
                "email": serializers.EmailField(),
            },
        )
    )
    def get_receiver(self, obj: BondRequest):
        return dict(
            id=obj.receiver.id,
            first_name=obj.receiver.first_name,
            email=obj.receiver.email,
        )

    def create(self, validated_data):
        return BondRequest.objects.create(**validated_data)
