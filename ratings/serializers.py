from rest_framework import serializers
from utils.serializers import CurrentUserDefaultSerializer

from . import models


class _RatingSerializer(
    CurrentUserDefaultSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.Rating
        fields = '__all__'


class StaffRatingSerializer(_RatingSerializer):
    pass


class UserRatingSerializer(_RatingSerializer):
    class Meta(_RatingSerializer.Meta):
        read_only_fields = ('user', )
