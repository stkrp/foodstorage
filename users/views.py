from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import (
    AllowAny, DjangoModelPermissionsOrAnonReadOnly
)
from django.contrib.auth.models import AnonymousUser
from photos.filters import PhotoRatingFilter
from lib.views.base import StaffOrUserView

from . import models
from . import serializers
from .permissions import UserOwnerOrReadOnlyPermission


class _UserAPIView(StaffOrUserView):
    # TODO: Добавить ссылку на страницу с фотографиями пользователя
    queryset = models.User.objects.all()
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    staff_serializer = serializers.UpdateUserStaffSerializer
    user_serializer = serializers.UpdateUserUserSerializer


class UserList(_UserAPIView, ListCreateAPIView):
    staff_serializer = serializers.CreateUserStaffSerializer
    user_serializer = serializers.CreateUserUserSerializer

    def get_permissions(self):
        if isinstance(self.request.user, AnonymousUser):
            return [AllowAny(), ]
        return super().get_permissions()


class UserDetail(_UserAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = _UserAPIView.permission_classes + (
        UserOwnerOrReadOnlyPermission,
    )


class PhotoRatingUserList(_UserAPIView, ListAPIView):
    """ Список пользователей, оценивших фотографию """
    filter_backends = (PhotoRatingFilter,)
