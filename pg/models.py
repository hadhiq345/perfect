from unicodedata import name
from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.PositiveIntegerField(unique=True)
    no_of_bed = models.IntegerField()

    def __str__(self) -> str:
        return str(self.room_no)


class Guest(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)    
    date_of_joining = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.mobile_no)


class RoomGuest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - {}".format(self.room, self.guest)