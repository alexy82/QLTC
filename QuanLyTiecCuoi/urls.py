from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse, path
from QuanLyTiecCuoi.views import customer
from QuanLyTiecCuoi.views import user, group, home, room, order
from QuanLyTiecCuoi.views.base import BaseITSAdminView

app_name = 'QuanLyTiecCuoi'


class ErrorView(BaseITSAdminView):
    def __init__(self):
        super(ErrorView, self).__init__()
        self.template_name = 'pages/error.html'


def logout_view(request):
    logout(request)
    return redirect(reverse('QuanLyTiecCuoi:index'))


urlpatterns = [
    path('', home.Home.as_view(), name='index'),
    path('logout/', logout_view, name='logout'),
    # path('error/', ErrorView.as_view(), name='error'),
    path('customers/', customer.CustomerListView.as_view(), name='customers'),
    path('customers/add/', customer.CustomerAddView.as_view(), name='customers-add'),
    path('customers/<int:id>/', customer.CustomerUpdateView.as_view(), name='customers-update'),
    path('orders/', order.OrderListView.as_view(), name='orders'),
    path('orders/add', order.OrderAddView.as_view(), name='orders-add'),
    path('orders/<int:id>', order.OrderAddView.as_view(), name='orders-detail'),

    # path('customers-type/', customer.CustomerTypeListView.as_view(), name='customers-type'),
    # path('customers-type/add/', customer.CustomerTypeAddView.as_view(), name='customers-type-add'),
    # path('customers-type/<int:id>/', customer.CustomerTypeUpdateView.as_view(), name='customers-type-update'),
    #
    path('rooms/', room.RoomListView.as_view(), name='rooms'),
    path('rooms/add/', room.RoomAddView.as_view(), name='room-add'),
    path('rooms/<int:id>/', room.RoomUpdateView.as_view(), name='rooms-update'),
    path('room-type/', room.RoomTypeListView.as_view(), name='room-type'),
    path('room-type/add/', room.RoomTypeAddView.as_view(), name='room-type-add'),
    path('room-type/<int:id>/', room.RoomTypeUpdateView.as_view(), name='room-type-update'),
    # path('stationeries/', merchandise.StationeryListView.as_view(), name='stationeries'),
    # path('stationeries/add/', merchandise.StationeryAddView.as_view(), name='stationeries-add'),
    # path('stationeries/<int:id>/', merchandise.StationeryUpdateView.as_view(), name='stationeries-update'),
    # path('stationeries-type/', merchandise.StationeryTypeListView.as_view(), name='stationeries-type'),
    # path('stationeries-type/add/', merchandise.StationeryTypeAddView.as_view(), name='stationeries-type-add'),
    # path('stationeries-type/<int:id>/', merchandise.StationeryTypeUpdateView.as_view(),
    #      name='stationeries-type-update'),
    #
    # path('suppliers/', supplier.SupplierListView.as_view(), name='suppliers'),
    # path('suppliers/add/', supplier.SupplierAddView.as_view(), name='suppliers-add'),
    # path('suppliers/<int:id>/', supplier.SupplierUpdateView.as_view(), name='suppliers-update'),
    #
    # path('promotions/', promotion.PromotionListView.as_view(), name='promotions'),
    #
    # path('delivery-note/add/', stock_transfer_in.StockTransferInAddView.as_view(), name='stock-transfer-in-add'),
    # path('delivery-note/<int:id>/', stock_transfer_in.StockTransferInDetailView.as_view(),
    #      name='stock-transfer-in-detail'),
    # path('delivery-note/', stock_transfer_in.StockTransferInListView.as_view(),
    #      name='stock-transfer-in'),
    #
    # path('receipt-note/add/', stock_transfer_out.StockTransferOutAddView.as_view(), name='stock-transfer-out-add'),
    # path('receipt-note/<int:id>/', stock_transfer_out.StockTransferOutDetailView.as_view(),
    #      name='stock-transfer-out-detail'),
    # path('receipt-note/', stock_transfer_out.StockTransferOutListView.as_view(),
    #      name='stock-transfer-out'),

    path('profile/', user.ProfileView.as_view(), name='profile'),
    path('groups/', group.GroupListView.as_view(), name='groups'),
    path('groups/add/', group.GroupAddView.as_view(), name='groups_add'),
    path('groups/<int:group_id>/', group.GroupEditView.as_view(), name='groups_detail'),
    path('users/', user.UserListView.as_view(), name='users'),
    path('users/<int:user_id>/', user.UserEditView.as_view(), name='users_detail'),
    path('users/add/', user.UserAddView.as_view(), name='users_add'),
    #
    # path('check/promotion/', check_promotion, name='promotions_check'),
]
