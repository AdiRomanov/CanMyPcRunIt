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
from .utils import search_games, search_game_by_name, get_cpu_by_model_name, get_gpu_by_model_name, \
    get_cpu_by_model_string
from .utils import get_gpu_by_model_string
import re
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


def determine_compatibility(pc_specs, game_specs):
    gpu, cpu, ram, os_version, storage = pc_specs.keys()

    # Print or use the variables
    """print("GPU:", pc_specs[gpu])
    print("CPU:", pc_specs[cpu])
    print("RAM:", pc_specs[ram])
    print("OS Version:", pc_specs[os_version])
    print("Storage:", pc_specs[storage])"""
    # print(pc_specs[cpu])
    # model_string = pc_specs[cpu]
    # user_cpu = get_cpu_by_model_name("Core i5 13600K")
    # user_cpu = get_cpu_by_model_name("Core i5-7400")

    model_string = "Model: Intel(R) Core(TM) Core i5 13600K CPU @ 3.00GHz"
    model_string = model_string.replace("Model:", "").split("@")[0].strip()
    user_cpu = get_cpu_by_model_string(model_string)
    # print(user_cpu.score)

    model_string = "Model: RTX 4080"
    model_string = model_string.replace("Model:", "").strip()
    user_gpu = get_gpu_by_model_string(model_string)
    # print(user_gpu.score)

    user_ram = pc_specs[ram]
    user_storage = pc_specs[storage]

    #
    #
    #

    # Assuming game_specs is a QuerySet
    game_specs = search_game_by_name(game_specs)  # Replace with your actual query

    # Convert the QuerySet to a list of dictionaries
    game_specs_list = list(game_specs.values())

    # Check if the list is not empty before accessing its elements
    if game_specs_list:
        # Extract 'ram_min', 'cpu_min', 'gpu_min', and 'storage_min' values
        ram_min_value = game_specs_list[0]['ram_min']
        cpu_min_values = game_specs_list[0]['cpu_min'].split('/')[0].strip()
        gpu_min_values = game_specs_list[0]['gpu_min'].split('/')[0].strip()
        storage_min_value = game_specs_list[0]['storage_min']

        model_string = "Core i5 12600K"
        model_string = model_string.replace("Model:", "").split("@")[0].strip()
        cpu_min = get_cpu_by_model_string(model_string)

        model_string = "GTX 950"
        model_string = model_string.replace("Model:", "").strip()
        gpu_min = get_gpu_by_model_string(model_string)

        if user_cpu.score >= cpu_min.score and user_gpu.score >= gpu_min.score:
            return True
    return False


@csrf_exempt  # This decorator is used to exempt the view from CSRF protection
@require_POST
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            parsed_data = json.loads(data)

            # to be changed
            dummy_game = "Red Dead Redemption 2"

            if determine_compatibility(parsed_data, dummy_game):
                print(f'Jocul {dummy_game} poate fi rulat de computerul dumneavoastra!')
            else:
                print(f'Jocul {dummy_game} nu poate fi rulat de computerul dumneavoastra!')

            # Process the received data as needed
            # For now, let's just print it
            print("Received data:", data)
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Unsupported HTTP method'})
