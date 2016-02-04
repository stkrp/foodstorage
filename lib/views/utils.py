from rest_framework.exceptions import NotFound


def model_instance_by_view_kwarg(view, pk_view_kwarg, model):
    """
    Получить объект по значению ключевого поля из CBV

    Пример:
    url(
        r'^(?P<user>\d+)/photos/$',
        UserPhotoList.as_view(),
        name='user-photo-list'
    )

    /2/photos/

    user = model_instance_by_view_kwarg(UserPhotoList_instance, 'user', User)
    user -> User instance with pk=2

    :param view:
    :param model:
    :param pk_view_kwarg:
    :return:
    :rtype: model or NoneType
    """
    pk = view.kwargs[pk_view_kwarg]
    try:
        obj = model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound(
            detail='{} instance with pk={} not found.'.format(
                model.__name__, pk
            )
        )
    return obj
