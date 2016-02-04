class StaffOrUserView(object):
    """
    Отдает staff_serializer "сотрудникам" и user_serializer "клиентам"
    """
    _SERIALIZER_ATTRS = ('staff_serializer', 'user_serializer')
    _REQUIRED_ATTRS = _SERIALIZER_ATTRS

    staff_serializer = None
    user_serializer = None

    @classmethod
    def _all_required_attrs_exists(cls):
        return all(hasattr(cls, attr) for attr in cls._REQUIRED_ATTRS)

    @classmethod
    def _serializers_are_not_none(cls):
        return all(
            getattr(cls, attr, None) is not None
            for attr in cls._SERIALIZER_ATTRS
        )

    def get_serializer_class(self):
        assert self._all_required_attrs_exists()
        assert self._serializers_are_not_none()

        if self.request.user.is_staff:
            return self.staff_serializer
        return self.user_serializer
