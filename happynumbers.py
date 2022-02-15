from digits import digits, integer, formatted


def happy_step(n, base=10):
    d = digits(n, base)
    return sum([x ** 2 for x in d])


def happy_sequence(n, base=10, max=10000):
    seq = [n]
    while len(seq) < max:
        n = happy_step(n, base)
        if n in seq:
            return seq
        seq.append(n)
    raise OverflowError('maximum sequence length exceed')


def is_happy(n, base=10):
    seq = happy_sequence(n, base)
    return seq[-1] == 1


def exhaustive_search(numbers, bases, filename):
    with open(filename, 'w') as output:
        for base in bases:
            output.write("BASE: {}".format(base))
            for n in numbers:
                if is_happy(n, base):
                    f = formatted(digits(n, base), base)
                    output.write("\n{} ({})".format(n, f))
            output.write("\n\n")
