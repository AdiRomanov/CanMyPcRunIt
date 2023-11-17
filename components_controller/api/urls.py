from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DummyGameView, GameViewSet, MinimumRequirementsViewSet, RecommendedRequirementsViewSet
from .views import SearchGameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'minimum-requirements', MinimumRequirementsViewSet)
router.register(r'recommended-requirements', RecommendedRequirementsViewSet)
router.register(r'search-game', SearchGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
