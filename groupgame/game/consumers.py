from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync, sync_to_async


class GameRoom(WebsocketConsumer):

    def connect(self):
        user_name = self.scope['url_route']['kwargs']['u_name']
        self.room_name = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = 'game_%s' % self.room_name
        print(user_name + 'connect socket')
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        user_name = json.loads(text_data).get('name')
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'users_active',
                'game_id': self.room_name,
                'u_name': user_name
            }
        )
    
    def users_active(self, event):
        print('event   ', event)
        users = event['u_name']
        self.send(text_data=json.dumps({
                'users': users
            }))
    

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print('disconnect socket')