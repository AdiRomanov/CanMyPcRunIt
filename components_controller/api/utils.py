# games/utils.py
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Game, CPU, GPU
import re


def search_games(query):
    """
    Funcție care returnează jocurile care corespund interogării specificate.
    """
    return Game.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(developer__icontains=query) |
        Q(ram_min__icontains=query) |
        Q(cpu_min__icontains=query) |
        Q(gpu_min__icontains=query) |
        Q(OS_min__icontains=query) |
        Q(storage_min__icontains=query) |
        Q(ram_rec__icontains=query) |
        Q(cpu_rec__icontains=query) |
        Q(gpu_rec__icontains=query) |
        Q(OS_rec__icontains=query) |
        Q(storage_rec__icontains=query)
    )


def search_game_by_name(name):
    """
    Funcție care returnează informațiile despre jocurile care conțin numele specificat.
    """
    return Game.objects.filter(name__icontains=name).values()


def get_cpu_by_model_name(model_name):
    # Retrieve the most matching CPU instance
    cpu = CPU.objects.filter(model__icontains=model_name).order_by('-model').first()
    # Raise a 404 error if no matching instance is found
    return get_object_or_404(CPU, pk=cpu.pk) if cpu else None


def get_cpu_by_model_string(model_string):
    # Define a regular expression pattern to match CPU model
    model_pattern = re.compile(r'\b([a-zA-Z0-9]+(?: [a-zA-Z0-9]+)+[^\s]+)\b', re.IGNORECASE)

    # Search for the model pattern in the provided string
    match = model_pattern.search(model_string)

    if match:
        # Extract the matched model
        model = match.group(1).strip()
    else:
        # If no match is found, return None or handle it accordingly
        return None

    # Retrieve all CPU instances
    all_cpus = CPU.objects.all()

    # Find the most matching CPU instance based on the number of matching characters
    best_matching_cpu = max(all_cpus, key=lambda cpu: sum(c1 == c2 for c1, c2 in zip(cpu.model.lower(), model.lower())))

    # Raise a 404 error if no matching instance is found
    return get_object_or_404(CPU, pk=best_matching_cpu.pk) if best_matching_cpu else None


def get_gpu_by_model_name(model_name):
    # Retrieve the most matching GPU instance
    gpu = GPU.objects.filter(model__icontains=model_name).order_by('-model').first()
    # Raise a 404 error if no matching instance is found
    return get_object_or_404(GPU, pk=gpu.pk) if gpu else None


def get_gpu_by_model_string(model_string):
    # Define a regular expression pattern to match GPU model
    model_pattern = re.compile(r'\b([a-zA-Z0-9]+(?: [a-zA-Z0-9]+)+[^\s]+)\b', re.IGNORECASE)

    # Search for the model pattern in the provided string
    match = model_pattern.search(model_string)

    if match:
        # Extract the matched model
        model = match.group(1).strip()
    else:
        # If no match is found, return None or handle it accordingly
        return None

    # Retrieve all GPU instances
    all_gpus = GPU.objects.all()

    # Find the most matching GPU instance based on the number of matching characters
    best_matching_gpu = max(all_gpus, key=lambda gpu: sum(c1 == c2 for c1, c2 in zip(gpu.model.lower(), model.lower())))

    # Raise a 404 error if no matching instance is found
    return get_object_or_404(GPU, pk=best_matching_gpu.pk) if best_matching_gpu else None
