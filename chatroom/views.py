from django.shortcuts import render, redirect
from chatroom.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(room=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def check(request):
    room = request.POST['room']
    username = request.POST['username']

    if Room.objects.filter(room=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(room=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(msg=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(room=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
