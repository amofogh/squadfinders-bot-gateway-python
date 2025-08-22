from django.contrib import admin
from .models import Player, Message, AIResponse
import json

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_date', 'platform', 'get_group_title', 'get_sender_username', 'players_count', 'game_mode', 'active']
    list_filter = ['platform', 'active', 'game_mode']
    search_fields = ['message_id', 'message']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []  # Disable ordering to avoid djongo issues

    fieldsets = (
        ('Message Info', {
            'fields': ('message_id', 'message_date', 'message')
        }),
        ('Sender Info', {
            'fields': ('sender',)
        }),
        ('Group Info', {
            'fields': ('group',)
        }),
        ('Game Info', {
            'fields': ('platform', 'rank', 'players_count', 'game_mode', 'active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_group_title(self, obj):
        if isinstance(obj.group, dict):
            return obj.group.get('group_title', 'N/A')
        return 'N/A'
    get_group_title.short_description = 'Group Title'

    def get_sender_username(self, obj):
        if isinstance(obj.sender, dict):
            return obj.sender.get('username', 'N/A')
        return 'N/A'
    get_sender_username.short_description = 'Username'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['sender', 'group']:
            kwargs['widget'] = admin.widgets.AdminTextareaWidget(attrs={'rows': 4, 'cols': 60})
            kwargs['help_text'] = 'Enter valid JSON format, e.g., {"username": "example", "id": 123}'
        return super().formfield_for_dbfield(db_field, request, **kwargs)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_date', 'get_group_title', 'get_sender_username', 'message_preview']
    search_fields = ['message_id', 'message']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []  # Disable ordering to avoid djongo issues
    
    fieldsets = (
        ('Message Info', {
            'fields': ('message_id', 'message_date', 'message')
        }),
        ('Sender Info', {
            'fields': ('sender',)
        }),
        ('Group Info', {
            'fields': ('group',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_group_title(self, obj):
        if isinstance(obj.group, dict):
            return obj.group.get('group_title', 'N/A')
        return 'N/A'
    get_group_title.short_description = 'Group Title'

    def get_sender_username(self, obj):
        if isinstance(obj.sender, dict):
            return obj.sender.get('username', 'N/A')
        return 'N/A'
    get_sender_username.short_description = 'Username'

    def message_preview(self, obj):
        return (obj.message[:50] + '...') if obj.message and len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['sender', 'group']:
            kwargs['widget'] = admin.widgets.AdminTextareaWidget(attrs={'rows': 4, 'cols': 60})
            kwargs['help_text'] = 'Enter valid JSON format, e.g., {"username": "example", "id": 123}'
        return super().formfield_for_dbfield(db_field, request, **kwargs)

@admin.register(AIResponse)
class AIResponseAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_preview', 'is_lfg', 'reason_preview']
    list_filter = ['is_lfg']
    search_fields = ['message_id', 'message', 'reason']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []  # Disable ordering to avoid djongo issues
    
    fieldsets = (
        ('AI Response Info', {
            'fields': ('message_id', 'message', 'is_lfg', 'reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def message_preview(self, obj):
        return (obj.message[:50] + '...') if obj.message and len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'

    def reason_preview(self, obj):
        return (obj.reason[:50] + '...') if obj.reason and len(obj.reason) > 50 else obj.reason
    reason_preview.short_description = 'Reason'