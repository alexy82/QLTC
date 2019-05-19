from django.db import models


class Customer(models.Model):
    """
    KHACHHANG(maKH,tenKH,soDiem,sdt,diaChi,email)
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=126, null=False, blank=False)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        app_label = "QuanLyTiecCuoi"
