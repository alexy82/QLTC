from rest_framework.viewsets import ModelViewSet
# from QuanLyTiecCuoi.serializers.stock_transfer_out import StockTransferOutDetailSerializer, StockTransferOutSerializer
# from QuanLyTiecCuoi.models.stock_transfer_out import StockTransferOutDetail, StockTransferOut
from datetime import datetime
import json
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from django.shortcuts import get_object_or_404, render
from datetime import datetime
# from QuanLyTiecCuoi.serializers.stock_transfer_in import StockTransferInDetailSerializer, StockTransferInSerializer
# from QuanLyTiecCuoi.models.stock_transfer_in import StockTransferInDetail, StockTransferIn
# from QuanLyTiecCuoi.models.merchandise import Merchandise
from QuanLyTiecCuoi.models.order import Order
from QuanLyTiecCuoi.models.room import Room
from QuanLyTiecCuoi.models.customer import Customer
from QLTC.middleware import get_current_user
# from QuanLyTiecCuoi.models.merchandise import Merchandise
# from QuanLyTiecCuoi.models.promotion import Promotion
from QuanLyTiecCuoi.serializers.order import OrderSerializer
from QuanLyTiecCuoi.views.base import BaseITSAdminView


class OrderListView(BaseITSAdminView):
    def __init__(self):
        super(OrderListView, self).__init__()
        self.template_name = 'pages/order_list.html'
        self.set_context_data(customer_list=Customer.objects.all(), user_list=User.objects.all(),
                              room_list=Room.objects.all())


class OrderAddView(BaseITSAdminView):
    def __init__(self):
        super(OrderAddView, self).__init__()
        self.template_name = 'pages/order_detail.html'
        self.set_context_data(rooms=Room.objects.all(), customers=Customer.objects.all(), action="Add",
                              url='/api/orders/', btn_content="Create")

class OrderUpdateView(BaseITSAdminView):
    def __init__(self):
        super(OrderUpdateView, self).__init__()
        self.template_name = 'pages/order_detail.html'
        self.set_context_data(action='Update', btn_content='Save',
                              rooms=Room.objects.all(), customers=Customer.objects.all())

    def get(self, request, id, **params):
        order = get_object_or_404(Order, pk=id)
        self.extra.update({"order": order,
                           "url": '/api/orders/{}/'.format(id),
                           })
        params.update(self.extra)
        return render(request, self.template_name, params)


# class StockTransferOutAddView(BaseITSAdminView):
#     def __init__(self):
#         super(StockTransferOutAddView, self).__init__()
#         self.template_name = 'pages/stock_transfer_out_detail.html'
#         self.set_context_data(books=Merchandise.objects.filter(merchandise_type=1, available_count__gt=0),
#                               stationeries=Merchandise.objects.filter(merchandise_type=0, available_count__gt=0),
#                               customers=Customer.objects.all())
#
#
# class OrderView(BaseITSAdminView):
#     def __init__(self):
#         super(StockTransferOutDetailView, self).__init__()
#         self.template_name = 'pages/stock_transfer_out_detail.html'
#
#     def get(self, request, id, **params):
#         note = get_object_or_404(StockTransferOut, pk=id)
#         self.extra.update({"note": note,
#                            "note_details": StockTransferOutDetail.objects.filter(inside=note)})
#         params.update(self.extra)
#         return render(request, self.template_name, params)

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
