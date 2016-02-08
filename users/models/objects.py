from django.contrib.auth.models import User, Group


DEFAULT_GROUPS = ['publisher', ]


def fetch_default_groups():
    return Group.objects.filter(name__in=DEFAULT_GROUPS)
