from rest_framework import serializers
from .models import DummyGame, Game, Info, MinimumRequirements, RecommendedRequirements


class DummyGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyGame
        fields = ('id', 'name', 'description', 'rating')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class MinimumRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimumRequirements
        fields = '__all__'


class RecommendedRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedRequirements
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    info = InfoSerializer()
    minimum_requirements = MinimumRequirementsSerializer()
    recommended_requirements = RecommendedRequirementsSerializer()

    class Meta:
        model = Game
        fields = '__all__'
