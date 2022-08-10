import http
from django.shortcuts import render
from django.http import HttpResponse

from pg.models import Room

def index(request):
    return HttpResponse('welcome to perfect pg')


def rooms_list_cheyyuka(request):
    rooms = Room.objects.all().order_by('-room_no')
    return render(request, 'rooms.html',{'rooms': rooms})

