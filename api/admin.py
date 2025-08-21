from django.contrib import admin
from .models import Player, Message, AIResponse

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['message_date', 'platform', 'get_group_title', 'get_sender_username', 'players_count', 'game_mode', 'active']
    list_filter = ['platform', 'active', 'message_date', 'game_mode']
    search_fields = ['message_id', 'message', 'sender__username', 'group__group_title']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []  # Disable default ordering to avoid ORDER BY issues
    
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
        return obj.group.get('group_title', 'N/A') if obj.group else 'N/A'
    get_group_title.short_description = 'Group Title'

    def get_sender_username(self, obj):
        return obj.sender.get('username', 'N/A') if obj.sender else 'N/A'
    get_sender_username.short_description = 'Username'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_date', 'get_group_title', 'get_sender_username', 'message_preview']
    search_fields = ['message_id', 'message', 'sender__username', 'group__group_title']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []  # Disable default ordering to avoid ORDER BY issues
    
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
        return obj.group.get('group_title', 'N/A') if obj.group else 'N/A'
    get_group_title.short_description = 'Group Title'

    def get_sender_username(self, obj):
        return obj.sender.get('username', 'N/A') if obj.sender else 'N/A'
    get_sender_username.short_description = 'Username'

    def message_preview(self, obj):
        return (obj.message[:50] + '...') if obj.message and len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'

@admin.register(AIResponse)
class AIResponseAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_preview', 'is_lfg', 'reason_preview']
    list_filter = ['is_lfg', 'created_at']
    search_fields = ['message_id', 'message', 'reason']
    readonly_fields = ['created_at', 'updated_at']
    ordering = []  # Disable default ordering to avoid ORDER BY issues
    
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