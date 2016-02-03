"""
https://docs.djangoproject.com/es/1.9/ref/models/expressions/#func-expressions
"""
from django.db.models.fields import IntegerField, FloatField
from django.db.models.expressions import Func


class Round(Func):
    # supports ROUND(column_name, decimals)
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, %(decimals)d)'

    def __init__(self, expression, decimals=0, **extra):
        assert isinstance(decimals, int)
        assert decimals >= 0

        output_field = extra.pop(
            'output_field', IntegerField() if decimals == 0 else FloatField()
        )
        super().__init__(
            expression, decimals=decimals, output_field=output_field, **extra
        )
