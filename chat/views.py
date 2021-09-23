from django.shortcuts import render, redirect
from chat.models import user, message
import json

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def chatRoom(request, roomName, username):
    userData = user.objects.get_or_create(name=username)
    Name = user.objects.get(name=username).name
    
    savedMessages = message.objects.filter(group=roomName)

    return render(request, 'chatRoom.html', { "roomName" : roomName, "username":Name , "messages": savedMessages}) 


def chatList(request, username):
    rooms = {}
    logUser = user.objects.get_or_create(name=username)
    currentUser = user.objects.get(name=username)
    chats = message.objects.filter(user=currentUser)
    for chat in chats:
        if chat.group not in rooms:
            allUsers = []
            rooms[chat.group] = set([str(message.user) for message in message.objects.filter(group=chat.group)])
    return render(request, 'chatList.html', {"rooms":rooms, "currentUser":currentUser})