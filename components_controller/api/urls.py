from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, search_game_by_name_view
from .views import SearchGameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)  # Setează ruta pentru resursa 'jocuri' utilizând GameViewSet
router.register(r'search-game', SearchGameViewSet)  # Setează ruta pentru resursa 'cauta-joc' utilizând SearchGameViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('search-game-by-name/<str:name>/', search_game_by_name_view, name='search-game-by-name'),
]
