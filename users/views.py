from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from lib.permissions import UserOwnerOrReadOnlyPermission
from lib.views.base import StaffOrUserView
from photos.filters import PhotoRatingFilter

from . import models
from . import serializers


class _UserAPIView(StaffOrUserView):
    queryset = models.User.objects.all()
    staff_serializer = serializers.StaffUserSerializer
    user_serializer = serializers.UserUserSerializer
    permissions_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    # TODO: Добавить ссылку на страницу с фотографиями пользователя


class UserList(_UserAPIView, ListCreateAPIView):
    pass


class UserDetail(_UserAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = _UserAPIView.permissions_classes + (
        UserOwnerOrReadOnlyPermission,
    )


class PhotoRatingUserList(_UserAPIView, ListAPIView):
    """ Список пользователей, оценивших фотографию """
    filter_backends = (PhotoRatingFilter,)
