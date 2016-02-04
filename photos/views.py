from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from users.filters import UserFilter, UserRatingFilter
from lib.permissions import UserOwnerOrReadOnlyPermission
from lib.views.base import StaffOrUserView

from . import models
from . import serializers


class _PhotoAPIView(StaffOrUserView):
    queryset = models.Photo.all_with_avg_rating()
    staff_serializer = serializers.StaffPhotoSerializer
    user_serializer = serializers.UserPhotoSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )


class PhotoList(_PhotoAPIView, ListCreateAPIView):
    pass


class PhotoDetail(_PhotoAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = _PhotoAPIView.permission_classes + (
        UserOwnerOrReadOnlyPermission,
    )


class UserPhotoList(_PhotoAPIView, ListAPIView):
    """ Список фотографий пользователя """
    filter_backends = (UserFilter, )


class UserRatingPhotoList(_PhotoAPIView, ListAPIView):
    """ Список фотографий, оцененных пользователем """
    filter_backends = (UserRatingFilter, )
