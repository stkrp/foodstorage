from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from utils.permissions import UserOwnerOrReadOnlyPermission
from utils.views import StaffOrUserView
from users.filters import UserFilter

from . import models
from . import serializers


class _PhotoAPIView(StaffOrUserView):
    queryset = models.Photo.all_with_avg_rating()
    staff_serializer = serializers.StaffPhotoSerializer
    user_serializer = serializers.UserPhotoSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    filter_backends = (UserFilter, )


class PhotoList(_PhotoAPIView, ListCreateAPIView):
    pass


class PhotoDetail(_PhotoAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = _PhotoAPIView.permission_classes + (
        UserOwnerOrReadOnlyPermission,
    )

# TODO: Сделать режим "только чтение" для /users/:id/photos/*
