from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .forms import GameSearchForm
from .models import Game
from .serializers import GameSerializer
from .utils import search_games, search_game_by_name

import json


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


@csrf_exempt
def get_csrf_token(request):
    if request.method == 'GET':
        csrf_token = request.COOKIES.get('csrftoken')
        return JsonResponse({'csrf_token': csrf_token})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt  # This decorator is used to exempt the view from CSRF protection
@require_POST
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            # Process the received data as needed
            # For now, let's just print it
            print("Received data:", data)
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Unsupported HTTP method'})
