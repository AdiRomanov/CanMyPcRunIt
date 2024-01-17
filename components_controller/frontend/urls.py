from django.urls import path
from .views import index

urlpatterns = [
    path('', index),  # Ruta pentru pagina principala
    path('search-game', index), # Ruta pentru pagina de căutare a jocurilor
    path('popular-games', index)  # Ruta pentru pagina de jocuri populare
]
