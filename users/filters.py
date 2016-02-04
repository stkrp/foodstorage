from rest_framework.filters import BaseFilterBackend
from lib.views.utils import model_instance_by_view_kwarg

from .models import User


class UserFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = model_instance_by_view_kwarg(view, 'user', User)
        if user is None:
            return queryset
        return queryset.filter(user=user)


class UserRatingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = model_instance_by_view_kwarg(view, 'user', User)
        if user is None:
            return queryset
        return queryset.filter(ratings__user=user)
