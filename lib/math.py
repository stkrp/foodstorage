from decimal import Decimal, ROUND_HALF_UP


def float_to_int(val, rounding=ROUND_HALF_UP):
    """
    Округлить float до целого числа

    По умолчанию используется классическое округление:

    1.51 -> 2
    1.5 -> 2
    1.49 -> 1

    -1.51 -> -2
    -1.5 -> -2
    -1.49 -> -1

    :param val:
    :param rounding:
    :return:
    """
    return int(Decimal(val).to_integral_value(rounding))
