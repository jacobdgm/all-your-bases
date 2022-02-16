import string

DIGIT_CHARACTERS = list(string.digits + string.ascii_uppercase + string.ascii_lowercase)


def digits(n, base=10):
    """Return a list of integers representing the digits of a given
number in a given base.

Digits are returned with the smallest place value first:
>>> digits(43, base=10)
[3, 4]"""
    if not _is_valid_base(base):
        raise ValueError("Base must be an integer greater than 1")

    if n == 0:
        return []
    else:
        quotient, remainder = divmod(n, base)
        return [remainder] + digits(quotient, base)


def integer(digits, base=10):
    """Given a list of integers representing digits of a number,
return the integer represented by those digits in the given
base.

Digits must be listed with the smallest place value first:
>>> integer([2, 1], base = 10)
12
"""
    if not _is_valid_base(base):
        raise ValueError("Base must be an integer greater than 1")
    
    place_values = range(len(digits))
    return sum(digits[i] * base ** i for i in place_values)


def formatted(digits, base=10):
    """Given a list of integers representing digits of a number,
return a string showing that number represented in the given base.

Uses the digits 0-9 for bases <= 10, adds uppercase letters for bases
<= 36, and adds lowercase letters for bases <= 62.

Digits must be listed with the smallest place value first:
>>> formatted([1, 2, 4], base = 10)
'421'
>>> thirty_one_in_16 = digits(31, base = 16)
>>> formatted(thirty_one_in_16, base = 16)
'1F'
"""
    if not _is_valid_base(base):
        raise ValueError("Base must be an integer greater than 1")
    if base > 62:
        raise ValueError("formatted() only supports bases less than or equal to 62")
    
    characters = [DIGIT_CHARACTERS[x] for x in digits[::-1]]
    return "".join(characters)


def _is_valid_base(base):
    return isinstance(base, int) and base > 1
