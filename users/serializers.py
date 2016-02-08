from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.hashers import make_password

from . import models


class _UserSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: Добавить валидацию поля "password"
    photos = serializers.SerializerMethodField()
    photos_ratings = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    ratings_photos = serializers.SerializerMethodField()

    class Meta:
        model = models.User

    def get_photos(self, obj):
        return reverse(
            'user-photo-list',
            kwargs={'user': obj.pk},
            request=self.context.get('request')
        )

    def get_photos_ratings(self, obj):
        return reverse(
            'user-photo-rating-list',
            kwargs={'user': obj.pk},
            request=self.context.get('request')
        )

    def get_ratings(self, obj):
        return reverse(
            'user-rating-list',
            kwargs={'user': obj.pk},
            request=self.context.get('request')
        )

    def get_ratings_photos(self, obj):
        return reverse(
            'user-rating-photo-list',
            kwargs={'user': obj.pk},
            request=self.context.get('request')
        )


class _StaffUserSerializer(_UserSerializer):
    class Meta(_UserSerializer.Meta):
        exclude = ('user_permissions', 'groups')


class _UserUserSerializer(_UserSerializer):
    class Meta(_UserSerializer.Meta):
        fields = (
            'url', 'username', 'email', 'first_name', 'last_name',
            'password'
        )


class _CreateUserSerializerMixin(object):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class _UpdateUserSerializerMixin(object):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }

    def update(self, user, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)
        return super().update(user, validated_data)


class CreateUserStaffSerializer(
    _CreateUserSerializerMixin, _StaffUserSerializer
):
    class Meta(_CreateUserSerializerMixin.Meta, _StaffUserSerializer.Meta):
        pass


class UpdateUserStaffSerializer(
    _UpdateUserSerializerMixin, _StaffUserSerializer
):
    class Meta(_UpdateUserSerializerMixin.Meta, _StaffUserSerializer.Meta):
        pass


class CreateUserUserSerializer(
    _CreateUserSerializerMixin, _UserUserSerializer
):
    class Meta(_CreateUserSerializerMixin.Meta, _UserUserSerializer.Meta):
        pass


class UpdateUserUserSerializer(
    _UpdateUserSerializerMixin, _UserUserSerializer
):
    class Meta(_UpdateUserSerializerMixin.Meta, _UserUserSerializer.Meta):
        pass
