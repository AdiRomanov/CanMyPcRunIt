from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('search-game', index),
    path('popular-games', index)
]
