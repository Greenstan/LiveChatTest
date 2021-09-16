from django.urls import re_path
from chat.consumers import ChatWsConsumer

websocketPatterns = [
    re_path(r'ws/chat/(?P<roomName>\w+)/$', ChatWsConsumer.as_asgi())
]