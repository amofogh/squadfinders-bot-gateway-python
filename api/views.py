from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Player, Message, AIResponse, AdminUser
from .serializers import PlayerSerializer, MessageSerializer, AIResponseSerializer, AdminUserSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
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
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
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
    queryset = AIResponse.objects.all()
    serializer_class = AIResponseSerializer
    
    def get_queryset(self):
        queryset = AIResponse.objects.all()
        is_lfg = self.request.query_params.get('is_lfg', None)
        
        if is_lfg is not None:
            is_lfg_bool = is_lfg.lower() == 'true'
            queryset = queryset.filter(is_lfg=is_lfg_bool)
            
        return queryset.order_by('-created_at')

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer