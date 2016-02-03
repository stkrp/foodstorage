from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):  # HyperlinkedModelSerializer
    # FIXME: Отсутствует хэширование пароля
    class Meta:
        model = models.User
        fields = '__all__'  # ('username', 'first_name', 'last_name')
