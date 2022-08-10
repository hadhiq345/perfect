from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import RoomSerializer
from rest_framework import generics
from pg.models import Room

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Create your views here.
def room_list(request):
    i = Room.objects.all().values()
    return JsonResponse(list(i), safe=False)
    