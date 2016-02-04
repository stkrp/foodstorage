from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from utils.permissions import UserOwnerOrReadOnlyPermission
from utils.views import StaffOrUserView

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
