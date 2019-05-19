from operator import attrgetter

from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer

from QLTC.middleware import get_current_request
from QuanLyTiecCuoi.models import Order, datetime, User
from QuanLyTiecCuoi.serializers.user import UserSerializer
from QuanLyTiecCuoi.serializers.customer import CustomerSerializer
from QuanLyTiecCuoi.serializers.room import RoomSerializer


class OrderSerializer(ModelSerializer):
    id = fields.CharField(required=False)
    customer_detail = CustomerSerializer(read_only=True, source='customer')
    created_by_detail = UserSerializer(read_only=True, source='created_by')
    room_detail = RoomSerializer(read_only=True, source='room')

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['date'] < datetime.datetime.now().date():
            raise serializers.ValidationError("Không được chọn ngày quá khứ")
        order = Order.objects.filter(date__exact=data['date'], at__exact=data['at'],
                                     room__id__exact=int(data['room'].id)).first()
        if order is not None:
            raise serializers.ValidationError("Phòng này đã được chọn")
        price = data['room'].price
        data['total'] = price
        data['deposit'] = price / 10
        return data


    class Meta:
        model = Order
        fields = '__all__'
