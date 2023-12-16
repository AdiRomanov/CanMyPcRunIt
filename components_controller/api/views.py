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
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        results = search_games(query)

        # Serialize the search results using your serializer
        serializer = self.get_serializer(results, many=True)

        return Response({'results': serializer.data})


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def search_game_by_name_view(request, name):
    results = search_game_by_name(name)
    # Process or format the results as needed
    return JsonResponse({'results': list(results)})




