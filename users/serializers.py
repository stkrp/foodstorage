from rest_framework import serializers

from . import models


class _UserSerializer(serializers.HyperlinkedModelSerializer):
    # FIXME: Отсутствует хэширование пароля
    class Meta:
        model = models.User
        # fields = '__all__'
        fields = ('url', 'username', 'email', 'first_name', 'last_name',)


class StaffUserSerializer(_UserSerializer):
    pass


class UserUserSerializer(_UserSerializer):
    pass
