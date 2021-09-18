from channels.generic.websocket import WebsocketConsumer 
import json
# The Consumer is synchronous but the channel layers are asynchronous 
from asgiref.sync import async_to_sync

from chat.models import message,user


# RUN docker run -p 6379:6379 -d redis:5 in terminal

class ChatWsConsumer (WebsocketConsumer):
    # class method to establish connection
    def connect(self):
        # collects connection details from the routing url 
        self.roomName = self.scope['url_route']["kwargs"]["roomName"]
        self.roomGroup = 'chat_{}'.format(self.roomName)

        # Establish the layer details and group to join 
        async_to_sync(self.channel_layer.group_add)(
        self.roomGroup ,
        self.channel_name
        )

        #Join 
        self.accept()

    # class method to disconnect from group 
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
        self.roomGroup ,
        self.channel_name
        )


    # class method to recieve message from the js websocket .send function 
    def receive(self, text_data):
        received = json.loads(text_data)
        message = received["message"]
        user = received["user"]
        room = received["room"]

        self.messToUser(user , message, room)


        async_to_sync(self.channel_layer.group_send)(
            self.roomGroup,
            {
                # type dictates which method the data is sent to
                'type': 'messageReceived',
                'message':message,
                'User': user,
                'room': room
            
        })
        # self.send(text_data = json.dumps({
        #     'message': message,
        #     'User': user
        # }))

# Receives data from receive method 
    def messageReceived(self, data):
        message = data['message']
        user = data['User']


        # Sends data back to websocket
        self.send(text_data = json.dumps({
            'message': message,
            'User': user
        }))
    
    # Method to save messages into new message objects 
    def messToUser(self, username, text, roomChat):

        message.objects.create(content=text, group=roomChat, user=user.objects.get(name=username))