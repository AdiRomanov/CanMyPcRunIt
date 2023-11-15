from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import DummyGame, Game, Info, MinimumRequirements, RecommendedRequirements
from .serializers import DummyGameSerializer, GameSerializer, InfoSerializer
from .serializers import MinimumRequirementsSerializer, RecommendedRequirementsSerializer


# Create your views here.

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
