from rest_framework import serializers
from rest_framework.reverse import reverse
from lib.serializers import CurrentUserDefaultSerializer

from . import models


class _PhotoSerializer(
    CurrentUserDefaultSerializer, serializers.HyperlinkedModelSerializer
):
    avg_rating = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    rating_users = serializers.SerializerMethodField()

    class Meta:
        model = models.Photo
        fields = '__all__'

    def get_avg_rating(self, obj):
        return obj.avg_rating

    def get_ratings(self, obj):
        return reverse(
            'photo-rating-list',
            kwargs={'photo': obj.pk},
            request=self.context.get('request')
        )

    def get_rating_users(self, obj):
        return reverse(
            'photo-rating-user-list',
            kwargs={'photo': obj.pk},
            request=self.context.get('request')
        )


class StaffPhotoSerializer(_PhotoSerializer):
    pass


class UserPhotoSerializer(_PhotoSerializer):
    class Meta(_PhotoSerializer.Meta):
        read_only_fields = ('user', )
