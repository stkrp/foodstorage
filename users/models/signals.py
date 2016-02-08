from .objects import fetch_default_groups


def _set_default_groups(user):
    user.groups.add(*fetch_default_groups())


def user_saved(sender, **kwargs):
    created = kwargs['created']
    if created:
        user = kwargs['instance']
        _set_default_groups(user)
