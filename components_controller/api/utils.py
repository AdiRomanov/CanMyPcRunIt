# games/utils.py
from django.db.models import Q
from .models import Game, CpuScore


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


def search_cpu_by_model(model):
    cpu = CpuScore.objects.filter(model__icontains=model).values()
    return cpu.score


def get_cpu_score(cpu_name):
    model = cpu_name.split(" ")[2].strip()
    return search_cpu_by_model(model)
