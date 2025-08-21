from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, MessageViewSet, AIResponseViewSet, AdminUserViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'airesponses', AIResponseViewSet, basename='airesponse')
router.register(r'adminusers', AdminUserViewSet, basename='adminuser')

urlpatterns = [
    path('', include(router.urls)),
]