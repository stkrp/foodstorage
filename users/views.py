from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from utils.permissions import UserOwnerOrReadOnlyPermission
from utils.views import StaffOrUserView

from . import models
from . import serializers


class _UserAPIView(StaffOrUserView):
    queryset = models.User.objects.all()
    staff_serializer = serializers.StaffUserSerializer
    user_serializer = serializers.UserUserSerializer
    permissions_classes = (DjangoModelPermissionsOrAnonReadOnly, )


class UserList(_UserAPIView, ListCreateAPIView):
    pass


class UserDetail(_UserAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = _UserAPIView.permissions_classes + (
        UserOwnerOrReadOnlyPermission,
    )
