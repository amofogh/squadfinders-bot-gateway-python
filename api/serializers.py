from rest_framework import serializers
from .models import Player, Message, AIResponse
import json

class PlayerSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'

    def get_sender(self, obj):
        return obj.get_sender()

    def get_group(self, obj):
        return obj.get_group()

    def create(self, validated_data):
        # Handle sender and group data
        sender_data = self.initial_data.get('sender', {})
        group_data = self.initial_data.get('group', {})
        
        # Remove sender and group from validated_data if they exist
        validated_data.pop('sender', None)
        validated_data.pop('group', None)
        
        player = Player.objects.create(**validated_data)
        player.set_sender(sender_data)
        player.set_group(group_data)
        player.save()
        
        return player

    def update(self, instance, validated_data):
        # Handle sender and group data
        sender_data = self.initial_data.get('sender')
        group_data = self.initial_data.get('group')
        
        # Remove sender and group from validated_data if they exist
        validated_data.pop('sender', None)
        validated_data.pop('group', None)
        
        # Update regular fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Update JSON fields if provided
        if sender_data is not None:
            instance.set_sender(sender_data)
        if group_data is not None:
            instance.set_group(group_data)
            
        instance.save()
        return instance

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_sender(self, obj):
        return obj.get_sender()

    def get_group(self, obj):
        return obj.get_group()

    def create(self, validated_data):
        # Handle sender and group data
        sender_data = self.initial_data.get('sender', {})
        group_data = self.initial_data.get('group', {})
        
        # Remove sender and group from validated_data if they exist
        validated_data.pop('sender', None)
        validated_data.pop('group', None)
        
        message = Message.objects.create(**validated_data)
        message.set_sender(sender_data)
        message.set_group(group_data)
        message.save()
        
        return message

    def update(self, instance, validated_data):
        # Handle sender and group data
        sender_data = self.initial_data.get('sender')
        group_data = self.initial_data.get('group')
        
        # Remove sender and group from validated_data if they exist
        validated_data.pop('sender', None)
        validated_data.pop('group', None)
        
        # Update regular fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Update JSON fields if provided
        if sender_data is not None:
            instance.set_sender(sender_data)
        if group_data is not None:
            instance.set_group(group_data)
            
        instance.save()
        return instance

class AIResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIResponse
        fields = '__all__'