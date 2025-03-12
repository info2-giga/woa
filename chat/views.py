from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser


class ChatRoom(View):
    template_name = "chat/chat_list.html"

def home(request, sender):
    return render(request, 'chat/chat_list.html', {"sender": sender})

@csrf_protect
def block_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        room = Room.objects.get(id=room_id)
        room.isBlocked = True
        room.save()
        return HttpResponse('Room blocked successfully')
    return HttpResponse('Invalid request', status=400)

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    is_blocked = room_details.isBlocked

    if not is_blocked:
        return render(request, 'chat/chat_room.html', {
            'username': username,
            'room': room,
            'room_details': room_details
        })
    else:
        return HttpResponse('You cannot send messages because you have either been blocked or blocked the user')

def checkview_get(request):
    room = request.GET.get('room_name')
    username = request.GET.get('username')

    parts = room.split(':;:')
    if len(parts) == 2:
        reversed_room = f"{parts[1]}:;:{parts[0]}"
    else:
        reversed_room = room

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    elif Room.objects.filter(name=reversed_room).exists():
        return redirect('/' + reversed_room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username='+ username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username' + username)

@login_required
def getRooms(request, user):
    # user_profile = get_object_or_404(CustomUser, username=user)
    activeRooms = Room.objects.filter(name__contains=user)
    # print(activeRooms)
    return JsonResponse({"rooms": list(activeRooms.values())})


def send(request):
    message = request.POST['message'],
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

