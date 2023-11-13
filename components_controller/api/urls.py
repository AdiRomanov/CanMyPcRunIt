from django.urls import path
from .views import DummyGameView

urlpatterns = [
    path('dummygame', DummyGameView.as_view()),
]
