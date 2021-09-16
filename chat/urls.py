from django.urls import path
from chat.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('chatRoom/<str:roomName>/<str:username>', chatRoom)
]
