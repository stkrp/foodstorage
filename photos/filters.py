from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import NotFound

from .models import Photo


class PhotoFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'photo' not in view.kwargs:
            return queryset
        photo = view.kwargs['photo']
        try:
            photo = Photo.objects.get(pk=photo)
        except Photo.DoesNotExist:
            raise NotFound(detail='Photo with pk={} not found.'.format(photo))
        return queryset.filter(user=photo)
