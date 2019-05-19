from django.contrib.auth.models import Permission, Group, User
from django.db.models import Q
from rest_framework import fields
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from QuanLyTiecCuoi.models.user_profile import Profile


class ProfileSerializer(ModelSerializer):
    id = fields.CharField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(ModelSerializer):
    id = fields.CharField(required=False)
    email = fields.EmailField(required=False)
    username = fields.CharField(required=False)
    first_name = fields.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = fields.CharField(required=False, allow_blank=True, allow_null=True)
    last_login = fields.DateTimeField(required=False)
    date_joined = fields.DateTimeField(required=False)
    is_active = fields.BooleanField(required=False, default=True)
    is_staff = fields.BooleanField(required=False, default=True)
    is_superuser = fields.BooleanField(required=False, default=True)
    groups_ids = PrimaryKeyRelatedField(required=False, many=True, read_only=False, queryset=Group.objects.all(),
                                        source='groups')
    permissions_ids = PrimaryKeyRelatedField(required=False, many=True, read_only=False,
                                             queryset=Permission.objects.filter(
                                                 Q(content_type__app_label='QuanLyTiecCuoi') | Q(
                                                     content_type__app_label='auth')),
                                             source='user_permissions')
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username','profile','email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active',
            'groups_ids', 'permissions_ids', 'is_staff', 'is_superuser')
        databases_always_serialize = (
            'id', 'username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active',
            'groups_ids','profile', 'permissions_ids', 'is_staff', 'is_superuser')
