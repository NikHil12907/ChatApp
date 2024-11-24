from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
from .models import Room, Message
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'chat/index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('room_list')
        else:
            messages.error(request, 'Invalid Username and Password')
    return render(request, 'chat/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form':form})
        
def logout_view(request):
    logout(request)


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'chat/room_list.html', {'rooms' : rooms})

@login_required
def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    rooms = Room.objects.all()
    return render(request, 'chat/room.html', {'room_name': room_name, 'rooms': rooms, 'username' : request.user.username})

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.creator = request.user
            room.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'chat/create_room.html', {'form': form})

@login_required
def delete_room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    
    if request.method == "POST":
        if request.user == room.creator:
            room.delete()
            messages.success(request, "Room Deleted Successfully")
        else:
            messages.error(request, "You are not authorized to delete this room")
        
    return redirect("room_list")   
