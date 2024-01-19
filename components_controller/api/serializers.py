from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    """
    Serializerul pentru modelul Game, folosit pentru a transforma obiectele Game în format JSON.
    """

    class Meta:
        model = Game
        fields = '__all__' # Include toate câmpurile modelului în serializare
