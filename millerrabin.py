from random import randrange


def modulo_exponentation(a, k, n):
    """
    :return: (a ** k) mod n
    """
    b = 1
    if k == 0:
        return b

    binary = '{0:b}'.format(k)
    if binary[-1] == '1':
        b = a

    tmp = a

    for i in range(len(binary) - 2, -1, -1):
        tmp = (tmp * tmp) % n
        if binary[i] == '1':
            b = (tmp * b) % n

    return b


def miller_rabin(n, t):
    """
    :param n: number to be checked
    :param t: number of rounds to check
    :return: True if n is a prime, False if is composite
    """
    s = 1
    while (n - 1) % (2 ** s):
        s += 1

    r = int((n - 1) / (2 ** s))
    picked = dict()

    for _ in range(t):
        a = randrange(2, n - 1)
        while a in picked:
            a = randrange(2, n - 1)
            picked[a] = 1

        y = modulo_exponentation(a, r, n)

        if y not in (1, n - 1):
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y ** 2) % n
                if y == 1:
                    return False
                j += 1

            if y != n - 1:
                return False

    return True
