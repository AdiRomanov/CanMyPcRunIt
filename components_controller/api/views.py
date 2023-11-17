from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import GameSearchForm
from .models import DummyGame, Game, Info, MinimumRequirements, RecommendedRequirements
from .serializers import DummyGameSerializer, GameSerializer, InfoSerializer
from .serializers import MinimumRequirementsSerializer, RecommendedRequirementsSerializer
from .utils import search_games


# Create your views here.

class SearchGameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()  # Replace 'Game' with your actual model
    serializer_class = GameSerializer  # Replace with your actual serializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        results = search_games(query)

        # Serialize the search results using your serializer
        serializer = self.get_serializer(results, many=True)

        return Response({'results': serializer.data})


class DummyGameView(generics.ListAPIView):
    queryset = DummyGame.objects.all()
    serializer_class = DummyGameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class MinimumRequirementsViewSet(viewsets.ModelViewSet):
    queryset = MinimumRequirements.objects.all()
    serializer_class = MinimumRequirementsSerializer


class RecommendedRequirementsViewSet(viewsets.ModelViewSet):
    queryset = RecommendedRequirements.objects.all()
    serializer_class = RecommendedRequirementsSerializer

