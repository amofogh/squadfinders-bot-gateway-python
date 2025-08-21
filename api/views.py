from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Player, Message, AIResponse
from .serializers import PlayerSerializer, MessageSerializer, AIResponseSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PlayerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Player records.
    
    Provides CRUD operations for players with filtering capabilities.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('platform', openapi.IN_QUERY, description="Filter by platform (PC, Console, unknown)", type=openapi.TYPE_STRING),
            openapi.Parameter('active', openapi.IN_QUERY, description="Filter by active status (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('game_mode', openapi.IN_QUERY, description="Filter by game mode (partial match)", type=openapi.TYPE_STRING),
        ]
    )
    def get_queryset(self):
        queryset = Player.objects.all()
        platform = self.request.query_params.get('platform', None)
        active = self.request.query_params.get('active', None)
        game_mode = self.request.query_params.get('game_mode', None)
        
        if platform is not None:
            queryset = queryset.filter(platform=platform)
        if active is not None:
            active_bool = active.lower() == 'true'
            queryset = queryset.filter(active=active_bool)
        if game_mode is not None:
            queryset = queryset.filter(game_mode__icontains=game_mode)
            
        return queryset.order_by('-message_date')

class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Message records.
    
    Provides CRUD operations for messages with filtering capabilities.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, description="Filter by sender username (partial match)", type=openapi.TYPE_STRING),
            openapi.Parameter('group_username', openapi.IN_QUERY, description="Filter by group username (partial match)", type=openapi.TYPE_STRING),
        ]
    )
    def get_queryset(self):
        queryset = Message.objects.all()
        username = self.request.query_params.get('username', None)
        group_username = self.request.query_params.get('group_username', None)
        
        if username is not None:
            queryset = queryset.filter(sender__username__icontains=username)
        if group_username is not None:
            queryset = queryset.filter(group__group_username__icontains=group_username)
            
        return queryset.order_by('-message_date')

class AIResponseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing AI Response records.
    
    Provides CRUD operations for AI responses with filtering capabilities.
    """
    queryset = AIResponse.objects.all()
    serializer_class = AIResponseSerializer
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('is_lfg', openapi.IN_QUERY, description="Filter by LFG status (true/false)", type=openapi.TYPE_BOOLEAN),
        ]
    )
    def get_queryset(self):
        queryset = AIResponse.objects.all()
        is_lfg = self.request.query_params.get('is_lfg', None)
        
        if is_lfg is not None:
            is_lfg_bool = is_lfg.lower() == 'true'
            queryset = queryset.filter(is_lfg=is_lfg_bool)
            
        return queryset.order_by('-created_at')