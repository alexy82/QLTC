import datetime

from django.db import models
from .customer import Customer
from .user_profile import User
from .room import Room


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    date = models.DateField(default=datetime.datetime.now().date())
    at = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0)

    class Meta:
        app_label = "QuanLyTiecCuoi"
