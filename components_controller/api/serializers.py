from rest_framework import serializers
from .models import DummyGame


class DummyGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyGame
        fields = ('id', 'name', 'description', 'rating')
