from django.urls import path
from api.views import room_list, RoomList

urlpatterns = [
    path('rooms', room_list ),
    path('rooms-drf', RoomList.as_view() ),
]