from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from lib.permissions import UserOwnerOrReadOnlyPermission
from lib.views.base import StaffOrUserView
from users.filters import UserFilter
from photos.filters import PhotoFilter

from . import models
from . import serializers


class _RatingAPIView(StaffOrUserView):
    queryset = models.Rating.objects.all().select_related('user', 'photo')
    staff_serializer = serializers.StaffRatingSerializer
    user_serializer = serializers.UserRatingSerializer
    permissions_classes = (DjangoModelPermissionsOrAnonReadOnly, )


class RatingList(_RatingAPIView, ListCreateAPIView):
    pass


class RatingDetail(_RatingAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = _RatingAPIView.permissions_classes + (
        UserOwnerOrReadOnlyPermission,
    )


class UserRatingList(_RatingAPIView, ListAPIView):
    """ Список оценок пользователя """
    filter_backends = (UserFilter, )


class PhotoRatingList(_RatingAPIView, ListAPIView):
    """ Список оценок фотографии """
    filter_backends = (PhotoFilter, )
