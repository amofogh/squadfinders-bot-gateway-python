from django.contrib import admin
from .models import Player, Message, AIResponse
import json

class JSONTextWidget(admin.widgets.AdminTextareaWidget):
    """Custom widget for JSON text fields"""
    def __init__(self, attrs=None):
        default_attrs = {'rows': 4, 'cols': 60, 'class': 'vLargeTextField'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_date', 'platform', 'get_group_title', 'get_sender_username', 'players_count', 'game_mode', 'active']
    list_filter = ['platform', 'active', 'game_mode']
    search_fields = ['message_id', 'message']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []

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
        try:
            group_data = obj.get_group()
            return group_data.get('group_title', 'N/A') if group_data else 'N/A'
        except Exception:
            return 'N/A'
    get_group_title.short_description = 'Group Title'

    def get_sender_username(self, obj):
        try:
            sender_data = obj.get_sender()
            return sender_data.get('username', 'N/A') if sender_data else 'N/A'
        except Exception:
            return 'N/A'
    get_sender_username.short_description = 'Username'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['sender', 'group']:
            kwargs['widget'] = JSONTextWidget()
            kwargs['help_text'] = 'Enter valid JSON format, e.g., {"username": "example", "id": 123}'
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        # Validate and save JSON fields
        try:
            if obj.sender:
                json.loads(obj.sender)  # Validate JSON
        except json.JSONDecodeError:
            obj.sender = '{}'
        
        try:
            if obj.group:
                json.loads(obj.group)  # Validate JSON
        except json.JSONDecodeError:
            obj.group = '{}'
        
        super().save_model(request, obj, form, change)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_date', 'get_group_title', 'get_sender_username', 'message_preview']
    search_fields = ['message_id', 'message']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []
    
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
        try:
            group_data = obj.get_group()
            return group_data.get('group_title', 'N/A') if group_data else 'N/A'
        except Exception:
            return 'N/A'
    get_group_title.short_description = 'Group Title'

    def get_sender_username(self, obj):
        try:
            sender_data = obj.get_sender()
            return sender_data.get('username', 'N/A') if sender_data else 'N/A'
        except Exception:
            return 'N/A'
    get_sender_username.short_description = 'Username'

    def message_preview(self, obj):
        return (obj.message[:50] + '...') if obj.message and len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['sender', 'group']:
            kwargs['widget'] = JSONTextWidget()
            kwargs['help_text'] = 'Enter valid JSON format, e.g., {"username": "example", "id": 123}'
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        # Validate and save JSON fields
        try:
            if obj.sender:
                json.loads(obj.sender)  # Validate JSON
        except json.JSONDecodeError:
            obj.sender = '{}'
        
        try:
            if obj.group:
                json.loads(obj.group)  # Validate JSON
        except json.JSONDecodeError:
            obj.group = '{}'
        
        super().save_model(request, obj, form, change)

@admin.register(AIResponse)
class AIResponseAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_preview', 'is_lfg', 'reason_preview']
    list_filter = ['is_lfg']
    search_fields = ['message_id', 'message', 'reason']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []
    
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