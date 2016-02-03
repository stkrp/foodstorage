from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from utils.permissions import UserOwnerOrReadOnlyPermission

from . import models
from . import serializers


class _PhotoAPIView(object):
    queryset = models.Photo.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.StaffPhotoSerializer
        return serializers.UserPhotoSerializer


class PhotoList(_PhotoAPIView, ListCreateAPIView):
    def perform_create(self, serializer):
        request_user = self.request.user
        serializer_user = serializer.validated_data.get('user', None)

        if serializer_user is None:
            serializer.save(request_user)
        else:
            serializer.save()


class PhotoDetail(_PhotoAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (
        DjangoModelPermissionsOrAnonReadOnly,
        UserOwnerOrReadOnlyPermission
    )
