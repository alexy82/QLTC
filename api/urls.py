from rest_framework import routers

from QuanLyTiecCuoi.views import group, user, room, customer, order

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'groups', group.GroupListViewSet, base_name='group_list'),
router.register(r'users', user.UserListViewSet, base_name='user_list'),
router.register(r'rooms', room.RoomViewSet, base_name='room_list'),
router.register(r'room-types', room.RoomTypeViewSet, base_name='room_types_list'),
router.register(r'customers', customer.CustomerViewSet, base_name='customer'),
router.register(r'orders', order.OrderViewSet, base_name='orders'),

