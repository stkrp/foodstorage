from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import NotFound

from .models import User


class UserFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'user' not in view.kwargs:
            return queryset
        user_pk = view.kwargs['user']
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise NotFound(detail='User with pk={} not found.'.format(user_pk))
        return queryset.filter(user=user)
