import random

from random import randrange
from util import *
from millerrabin import miller_rabin


def random_search(k, t):
    first = 10 ** (k - 1)
    last = 10 ** k

    while True:
        n = randrange(first + 1, last - 1, step=2)

        if division_with_primes_test(n) and miller_rabin(n, t):
            return n


def random_search_congruence_sieve(k, t):
    first = 10 ** (k - 1)
    last = 10 ** k

    while True:
        n = randrange(first + 1, last - 1, step=2)

        if n % 3 != 2:
            continue

        if division_with_primes_test(n) and miller_rabin(n, t):
            return n


def random_search_small_primes_sieve(k, t):
    first = 10 ** (k - 1)
    last = 10 ** k

    while True:
        n = randrange(first + 1, last - 1, step=2)

        good = True
        for i in range(5):
            r = B[i]
            p = DIVS[i]
            if n % r == p:
                good = False
                break

        if not good:
            continue

        if division_with_primes_test(n) and miller_rabin(n, t):
            return n


def random_search_combined_sieves(k, t):
    first = 10 ** (k - 1)
    last = 10 ** k

    while True:
        n = randrange(first + 1, last - 1, step=2)

        if n % 3 != 2:
            continue

        good = True

        w = int((n - 1) / 2)

        for i in range(5):
            r = B[i]
            p = DIVS[i]
            if n % r == p:
                good = False
                break

        if not good:
            continue

        if division_with_primes_test(n) and miller_rabin(n, t):
            return n
