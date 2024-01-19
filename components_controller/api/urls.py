from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, search_game_by_name_view
from .views import SearchGameViewSet
from .views import get_csrf_token
from .views import receive_data

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'search-game', SearchGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search-game-by-name/<str:name>/', search_game_by_name_view, name='search-game-by-name'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('receive-data/', receive_data, name='receive_data'),
]
