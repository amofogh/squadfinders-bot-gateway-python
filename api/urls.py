from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, MessageViewSet, AIResponseViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'airesponses', AIResponseViewSet, basename='airesponse')

urlpatterns = [
    path('', include(router.urls)),
]