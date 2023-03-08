from rest_framework import serializers
from .models import BondRequest


class BondRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BondRequest
        fields = "__all__"
