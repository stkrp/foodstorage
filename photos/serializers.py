from rest_framework import serializers

from . import models


class _PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'


class StaffPhotoSerializer(_PhotoSerializer):
    pass


class UserPhotoSerializer(_PhotoSerializer):
    class Meta(_PhotoSerializer.Meta):
        read_only_fields = ('user', )
