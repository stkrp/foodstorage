from rest_framework import serializers

from . import models


class _PhotoSerializer(serializers.HyperlinkedModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Photo
        fields = '__all__'

    def get_avg_rating(self, obj):
        return obj.avg_rating


class StaffPhotoSerializer(_PhotoSerializer):
    pass


class UserPhotoSerializer(_PhotoSerializer):
    class Meta(_PhotoSerializer.Meta):
        read_only_fields = ('user', )
