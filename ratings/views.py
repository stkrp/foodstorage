from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from utils.permissions import UserOwnerOrReadOnlyPermission
from utils.views import StaffOrUserView
from users.filters import UserFilter

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


class _UserRatingAPIView(_RatingAPIView):
    filter_backends = (UserFilter, )


class UserRatingList(_UserRatingAPIView, ListAPIView):
    """ Список оценок пользователя """
    pass
