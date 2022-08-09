from django.contrib import admin

# Register your models here.
from pg.models import Room, Guest, RoomGuest
admin.site.register([Room, Guest, RoomGuest])