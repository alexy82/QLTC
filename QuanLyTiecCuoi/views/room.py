from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from QuanLyTiecCuoi.serializers.room import RoomSerializer, RoomTypeSerializer
from QuanLyTiecCuoi.models.room import RoomType, Room
# from QuanLyNhaSach.models.stock_transfer_in import StockTransferInDetail, StockTransferIn
# from QuanLyNhaSach.models.stock_transfer_out import StockTransferOutDetail
from QuanLyTiecCuoi.views.base import BaseITSAdminView


class RoomListView(BaseITSAdminView):
    def __init__(self):
        super(RoomListView, self).__init__()
        self.template_name = 'pages/room_list.html'
        self.set_context_data(room_type=RoomType.objects.all())


class RoomAddView(BaseITSAdminView):
    def __init__(self):
        super(RoomAddView, self).__init__()
        self.template_name = 'pages/room_detail.html'
        self.set_context_data(room_type=RoomType.objects.all(), action="Add",
                              url='/api/rooms/', btn_content="Create")


class RoomUpdateView(BaseITSAdminView):
    def __init__(self):
        super(RoomUpdateView, self).__init__()
        self.template_name = 'pages/room_detail.html'
        self.set_context_data(action='Update', btn_content='Save',
                              room_type=RoomType.objects.all())

    def get(self, request, id, **params):
        room = get_object_or_404(Room, pk=id)
        self.extra.update({"room": room,
                           "url": '/api/rooms/{}/'.format(id),
                           # "note_in_list": StockTransferInDetail.objects.select_related('inside').filter(unit__id=id),
                           # "note_out_list": StockTransferOutDetail.objects.select_related('inside').filter(
                           #     unit__id=id)
                           })
        params.update(self.extra)
        return render(request, self.template_name, params)


class RoomTypeListView(BaseITSAdminView):
    def __init__(self):
        super(RoomTypeListView, self).__init__()
        self.template_name = 'pages/room_type_list.html'


class RoomTypeUpdateView(BaseITSAdminView):
    def __init__(self):
        super(RoomTypeUpdateView, self).__init__()
        self.template_name = 'pages/room_type_detail.html'
        self.set_context_data(action='Update', btn_content='Save')

    def get(self, request, id, **params):
        type = get_object_or_404(RoomType, pk=id)
        self.extra.update({"type": type,
                           "url": '/api/room-types/{}/'.format(id)})
        params.update(self.extra)
        return render(request, self.template_name, params)


class RoomTypeAddView(BaseITSAdminView):
    def __init__(self):
        super(RoomTypeAddView, self).__init__()
        self.template_name = 'pages/room_type_detail.html'
        self.set_context_data(action="Add", url='/api/room-types/', btn_content="Create")


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomTypeViewSet(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

