import json
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room,Message
from django.utils.timezone import now

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = "chat_%s" % self.room_name

        self.user = self.scope['user']
        # Join The Room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        timestamp = now().strftime("%H:%M")
        
        await self.save_message(self.user.username, message, self.room_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username': self.user.username,
                'timestamp':timestamp
                
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        timestamp = event['timestamp']

        await self.send(text_data=json.dumps({
            'message':message,
            'username': username,
            'timestamp': timestamp
            
        }))

    @database_sync_to_async
    def save_message(self, username, message, room_name):
        room = Room.objects.get(name=room_name)
        user = User.objects.get(username=username)
        Message.objects.create(room=room, user=user, content=message)  