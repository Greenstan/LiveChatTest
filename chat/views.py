from django.shortcuts import render, redirect
from chat.models import user, message

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def chatRoom(request, roomName, username):
    userData = user.objects.get_or_create(name=username)
    Name = user.objects.get(name=username).name
    
    savedMessages = message.objects.filter(group=roomName)

    print(Name,"and",username)

    return render(request, 'chatRoom.html', { "roomName" : roomName, "username":Name , "messages": savedMessages}) 


def deleteMessage (request, roomName, username):
    message.objects.filter(group=roomName).delete()
    return redirect("/chatRoom/{0}/{1}".format(roomName,username))