from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from lib.views.base import StaffOrUserView
from photos.filters import PhotoRatingFilter

from . import models
from . import serializers
from .permissions import UserOwnerOrReadOnlyPermission


class _UserAPIView(StaffOrUserView):
    queryset = models.User.objects.all()
    staff_serializer = serializers.StaffUserSerializer
    user_serializer = serializers.UserUserSerializer
    # TODO: Добавить ссылку на страницу с фотографиями пользователя


class UserList(_UserAPIView, ListCreateAPIView):
    pass


class UserDetail(_UserAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (UserOwnerOrReadOnlyPermission, )


class PhotoRatingUserList(_UserAPIView, ListAPIView):
    """ Список пользователей, оценивших фотографию """
    filter_backends = (PhotoRatingFilter,)
