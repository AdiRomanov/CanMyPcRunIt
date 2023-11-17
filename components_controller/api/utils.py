# games/utils.py
from django.db.models import Q
from .models import Game

"""
query = "name1"
results = Game.objects.filter(info__name__icontains=query)
print(f"Rezultat gasit {results}")
"""


def search_games(query):
    return Game.objects.filter(
        Q(info__name__icontains=query) |
        Q(info__description__icontains=query) |
        Q(info__developer__icontains=query)
    )
