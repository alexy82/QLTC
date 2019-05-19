from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from QuanLyTiecCuoi.models.room import Room, RoomType


class RoomTypeSerializer(ModelSerializer):
    id = fields.CharField(required=False)

    class Meta:
        model = RoomType
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    id = fields.CharField(required=False)
    type = RoomTypeSerializer(read_only=True,source='room_type')

    class Meta:
        model = Room
        fields = '__all__'
