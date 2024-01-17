from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import GameSearchForm
from .models import Game
from .serializers import GameSerializer
from .utils import search_games, search_game_by_name


# Create your views here.

class SearchGameViewSet(viewsets.ModelViewSet):
    """
    Setul de vederi care gestionează operațiile legate de căutarea jocurilor.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Metodă de acțiune pentru căutarea jocurilor bazată pe parametrul de interogare 'q'.
        Returnează rezultatele căutării sub formă de răspuns JSON.
        """

        query = request.query_params.get('q', '')
        results = search_games(query)

        # Serializarea rezultatelor căutării folosind serializerul definit
        serializer = self.get_serializer(results, many=True)

        return Response({'results': serializer.data})


class GameViewSet(viewsets.ModelViewSet):
    """
    Setul de vederi care gestionează operațiile CRUD pentru modelul Game.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


def search_game_by_name_view(request, name):
    """
    Vederea care returnează rezultatele căutării după nume sub formă de răspuns JSON.
    """

    results = search_game_by_name(name)
    # Procesează sau formatează rezultatele după necesități
    return JsonResponse({'results': list(results)})




