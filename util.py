import math

B = [3]
DIVS = [1]


def is_prime(n):
    for x in range(2, int(math.sqrt(n)) + 1):
        if not n % x:
            return False

    return True


def compute_b(limit):
    global B, DIVS
    for i in range(3, limit):
        if is_prime(i):
            B.append(i)
            DIVS.append(int((i - 1) / 2))


def division_with_primes_test(n):
    for p in B:
        if n % p == 0:
            return False

    return True
