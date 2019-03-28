from rest_framework import serializers
from stuapp.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    """演员序列化器"""
    class Meta:
        model = Actor
        fields = '__all__'