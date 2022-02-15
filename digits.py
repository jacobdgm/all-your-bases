import string

DIGIT_CHARACTERS = list(string.digits + string.ascii_uppercase + string.ascii_lowercase)


def digits(n, base=10):
    """Return a list of integers representing the digits of a given
    number in a given base. Digits are returned with the smallest place
    value first:

    >>> digits(43, base=10)
    [3, 4]"""
    _check_base(base)
    if n == 0:
        return []
    else:
        quotient, remainder = divmod(n, base)
        return [remainder] + digits(quotient, base)


def integer(digits, base=10):
    """Given a list of integers representing digits of a number,
    return the integer represented by those digits in the given
    base. Digits must be listed with the smallest place value first:

    >>> integer([2, 1], base = 10)
    12
    """
    _check_base(base)
    place_values = range(len(digits))
    return sum(digits[i] * base ** i for i in place_values)


def formatted(digits, base=10):
    characters = [DIGIT_CHARACTERS[x] for x in digits[::-1]]
    return "".join(characters)


def _check_base(base):
    if not isinstance(base, int) or base <= 1:
        raise ValueError("Base must be an integer greater than 1")
