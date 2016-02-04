from rest_framework.fields import CurrentUserDefault


class CurrentUserDefaultSerializer(object):
    """
    Устанавливает пользователя, отправившего запрос, автором записи,
    если другой пользователь не передан в запросе.

    """
    user_field_name = 'user'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_field = self.fields.get(self.user_field_name, None)
        if user_field is not None:
            user_field.default = CurrentUserDefault()
