from django.db import models


class RoomType(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=126, null=False, blank=False)
    desc = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        app_label = "QuanLyTiecCuoi"


class Room(models.Model):


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=126, null=False, blank=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        app_label = "QuanLyTiecCuoi"
