from rest_framework.filters import BaseFilterBackend
from lib.views.utils import model_instance_by_view_kwarg

from .models import Photo


class PhotoFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        photo = model_instance_by_view_kwarg(view, 'photo', Photo)
        if photo is None:
            return queryset
        return queryset.filter(photo=photo)


class PhotoRatingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        photo = model_instance_by_view_kwarg(view, 'photo', Photo)
        if photo is None:
            return queryset
        return queryset.filter(ratings__photo=photo)
