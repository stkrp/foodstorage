from rest_framework import serializers
from rest_framework import permissions
from django.contrib.auth.hashers import make_password

from . import models


# TODO: Перечитать
class _UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }
        # http://www.django-rest-framework.org/api-guide/permissions/#allowany

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, user, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)
        return super().update(user, validated_data)


class StaffUserSerializer(_UserSerializer):
    class Meta(_UserSerializer.Meta):
        exclude = ('user_permissions', )


class UserUserSerializer(_UserSerializer):
    class Meta(_UserSerializer.Meta):
        fields = (
            'url', 'username', 'email', 'first_name', 'last_name',
            'password'
        )
        permission_classes = (permissions.AllowAny, )
