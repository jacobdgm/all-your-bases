def digits(n, base=10):
    """Return a list of integers representing the digits of a given
    number in a given base. Digits are returned with the smallest place
    value first:

    >>> digits(43, base=10)
    [3, 4]"""
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
    place_values = range(len(digits))
    return sum(map(lambda i: digits[i] * base ** i, place_values))
