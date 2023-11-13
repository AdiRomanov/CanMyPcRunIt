from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import DummyGame
from .serializers import DummyGameSerializer


# Create your views here.

class DummyGameView(generics.ListAPIView):
    queryset = DummyGame.objects.all()
    serializer_class = DummyGameSerializer
