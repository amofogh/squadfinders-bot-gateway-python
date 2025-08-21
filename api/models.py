from djongo import models
import json

class Player(models.Model):
    _id = models.ObjectIdField()
    message_id = models.IntegerField(unique=True, db_index=True)
    message_date = models.DateTimeField()
    sender = models.JSONField(default=dict)
    group = models.JSONField(default=dict)
    message = models.TextField(null=True, blank=True)
    platform = models.CharField(
        max_length=20,
        choices=[
            ('PC', 'PC'),
            ('Console', 'Console'),
            ('unknown', 'Unknown'),
        ],
        default='unknown'
    )
    rank = models.CharField(max_length=255, null=True, blank=True)
    players_count = models.IntegerField(null=True, blank=True)
    game_mode = models.CharField(max_length=255, default='')
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'players'

    def __str__(self):
        return f"Player {self.message_id} - {self.sender.get('username', 'Unknown')}"

class Message(models.Model):
    _id = models.ObjectIdField()
    message_id = models.IntegerField(unique=True, db_index=True)
    message_date = models.DateTimeField()
    sender = models.JSONField(default=dict)
    group = models.JSONField(default=dict)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f"Message {self.message_id} - {self.sender.get('username', 'Unknown')}"

class AIResponse(models.Model):
    _id = models.ObjectIdField()
    message_id = models.IntegerField(unique=True, db_index=True)
    message = models.TextField(null=True, blank=True)
    is_lfg = models.BooleanField(default=False)
    reason = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'airesponses'

    def __str__(self):
        return f"AI Response {self.message_id} - LFG: {self.is_lfg}"