from django.contrib.auth.models import Permission, Group, User
from django.db.models import Q
from rest_framework import fields
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer


class GroupSerializer(ModelSerializer):
    id = fields.CharField(required=False)
    name = fields.CharField(required=True)
    permissions_ids = PrimaryKeyRelatedField(many=True, read_only=False, queryset=Permission.objects.filter(
        Q(content_type__app_label='QuanLyTiecCuoi') | Q(content_type__app_label='auth')),
                                             source='permissions')

    class Meta:
        model = Group
        fields = (
            'id', 'name', 'permissions_ids')
        databases_always_serialize = (
            'id', 'name', 'permissions_ids')
