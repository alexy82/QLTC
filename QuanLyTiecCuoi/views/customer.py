from django.shortcuts import reverse, get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from QuanLyTiecCuoi.serializers.customer import CustomerSerializer
from QuanLyTiecCuoi.models.customer import Customer
from QuanLyTiecCuoi.views.base import BaseITSAdminView


# from QuanLyTiecCuoi.models.stock_transfer_out import StockTransferOut


class CustomerListView(BaseITSAdminView):
    def __init__(self):
        super(CustomerListView, self).__init__()
        self.template_name = 'pages/customer_list.html'


class CustomerAddView(BaseITSAdminView):
    def __init__(self):
        super(CustomerAddView, self).__init__()
        self.template_name = 'pages/customer_detail.html'
        self.set_context_data(action='Add', url='/api/customers/', btn_content='Create')


class CustomerUpdateView(BaseITSAdminView):
    def __init__(self):
        super(CustomerUpdateView, self).__init__()
        self.template_name = 'pages/customer_detail.html'
        self.set_context_data(action='Update', btn_content='Save')

    def get(self, request, id, **params):
        customer = get_object_or_404(Customer, pk=id)
        self.extra.update({"customer": customer,
                           "url": '/api/customers/{}/'.format(id),
                           # "note_out_list": StockTransferOut.objects.filter(customer__id=id)
                           }
                          )
        params.update(self.extra)
        return render(request, self.template_name, params)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
