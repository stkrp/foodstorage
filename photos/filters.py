from rest_framework.filters import BaseFilterBackend
from lib.views.utils import model_instance_by_view_kwarg

from .models import Photo


class PhotoFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        photo = model_instance_by_view_kwarg(view, 'photo', Photo)
        return queryset.filter(photo=photo)


class PhotoRatingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        """
        Выбирает все записи, которые оценивали фото

        Например, выбирает всех пользователей, которые оценивали фото.
        """
        photo = model_instance_by_view_kwarg(view, 'photo', Photo)
        return queryset.filter(ratings__photo=photo)
