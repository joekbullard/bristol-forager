from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "records")
