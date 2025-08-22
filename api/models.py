from djongo import models
import json

class Player(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, serialize=False)
    message_id = models.IntegerField(unique=True, db_index=True)
    message_date = models.DateTimeField()
    sender = models.TextField(default='{}', blank=True)  # Store JSON as text
    group = models.TextField(default='{}', blank=True)   # Store JSON as text
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
    game_mode = models.CharField(max_length=255, default='', blank=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'players'

    def get_sender(self):
        """Get sender as dict"""
        try:
            return json.loads(self.sender) if self.sender else {}
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_sender(self, value):
        """Set sender from dict"""
        self.sender = json.dumps(value) if value else '{}'

    def get_group(self):
        """Get group as dict"""
        try:
            return json.loads(self.group) if self.group else {}
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_group(self, value):
        """Set group from dict"""
        self.group = json.dumps(value) if value else '{}'

    def __str__(self):
        try:
            sender_data = self.get_sender()
            sender_username = sender_data.get('username', 'Unknown') if sender_data else 'Unknown'
            return f"Player {self.message_id} - {sender_username}"
        except Exception:
            return f"Player {self.message_id}"

class Message(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, serialize=False)
    message_id = models.IntegerField(unique=True, db_index=True)
    message_date = models.DateTimeField()
    sender = models.TextField(default='{}', blank=True)  # Store JSON as text
    group = models.TextField(default='{}', blank=True)   # Store JSON as text
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'messages'

    def get_sender(self):
        """Get sender as dict"""
        try:
            return json.loads(self.sender) if self.sender else {}
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_sender(self, value):
        """Set sender from dict"""
        self.sender = json.dumps(value) if value else '{}'

    def get_group(self):
        """Get group as dict"""
        try:
            return json.loads(self.group) if self.group else {}
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_group(self, value):
        """Set group from dict"""
        self.group = json.dumps(value) if value else '{}'

    def __str__(self):
        try:
            sender_data = self.get_sender()
            sender_username = sender_data.get('username', 'Unknown') if sender_data else 'Unknown'
            return f"Message {self.message_id} - {sender_username}"
        except Exception:
            return f"Message {self.message_id}"

class AIResponse(models.Model):
    _id = models.ObjectIdField(auto_created=True, primary_key=True, serialize=False)
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