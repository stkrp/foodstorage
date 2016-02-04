from rest_framework import serializers
from lib.serializers import CurrentUserDefaultSerializer

from . import models


class _RatingSerializer(
    CurrentUserDefaultSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = models.Rating
        fields = '__all__'

    def validate(self, data):
        data = super().validate(data)
        if data['user'] == data['photo'].user:
            raise serializers.ValidationError(
                'Rater must not be the owner of photo.'
            )
        return data


class StaffRatingSerializer(_RatingSerializer):
    pass


class UserRatingSerializer(_RatingSerializer):
    class Meta(_RatingSerializer.Meta):
        read_only_fields = ('user', )
