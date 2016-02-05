from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.permissions import SAFE_METHODS


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


def get_action_type(request):
    method = request.method
    if method in SAFE_METHODS:
        return 'view'
    elif method == 'POST':
        return 'create'
    elif method == 'DELETE':
        return 'delete'
    elif method in ('PUT', 'PATCH'):
        return 'update'
    else:
        raise MethodNotAllowed(method)
