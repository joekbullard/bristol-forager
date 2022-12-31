from .models import CustomUser
from rest_framework import serializers
from forager.models import Record

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.StringRelatedField(
        many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'records')

    