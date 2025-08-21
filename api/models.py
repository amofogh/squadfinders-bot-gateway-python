from djongo import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import json

class SenderInfo(models.Model):
    id = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(
        max_length=20,
        choices=[
            ('unknown', 'Unknown'),
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        default='unknown'
    )
    
    class Meta:
        abstract = True

class GroupInfo(models.Model):
    group_id = models.CharField(max_length=255, null=True, blank=True)
    group_title = models.CharField(max_length=255, null=True, blank=True)
    group_username = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        abstract = True

class Player(models.Model):
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
        indexes = [
            models.Index(fields=['message_id']),
        ]

    def __str__(self):
        return f"Player {self.message_id} - {self.sender.get('username', 'Unknown')}"

class Message(models.Model):
    message_id = models.IntegerField(unique=True, db_index=True)
    message_date = models.DateTimeField()
    sender = models.JSONField(default=dict)
    group = models.JSONField(default=dict)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'messages'
        indexes = [
            models.Index(fields=['message_id']),
        ]

    def __str__(self):
        return f"Message {self.message_id} - {self.sender.get('username', 'Unknown')}"

class AIResponse(models.Model):
    message_id = models.IntegerField(unique=True, db_index=True)
    message = models.TextField(null=True, blank=True)
    is_lfg = models.BooleanField(default=False)
    reason = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'airesponses'
        indexes = [
            models.Index(fields=['message_id']),
        ]

    def __str__(self):
        return f"AI Response {self.message_id} - LFG: {self.is_lfg}"

class AdminUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('viewer', 'Viewer'),
        ]
    )

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'adminusers'

    def __str__(self):
        return f"{self.email} - {self.role}"