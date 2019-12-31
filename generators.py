from util import *
from randomsearch import random_search, random_search_combined_sieves, random_search_small_primes_sieve,\
    random_search_congruence_sieve, random_search_combined_naccache
from millerrabin import miller_rabin


def naive_method(k, t=10):
    step = (10 ** (k - 1)) / 2
    while True:
        q = random_search(k - 1, t)
        # if q <= step:
        #    continue

        p = 2 * q + 1

        if division_with_primes_test(p) and miller_rabin(p, t):
            return p


visited_naccache = dict()
def naive_method_naccache(k, t=10):
    global visited_naccache
    step = (10 ** (k - 1)) / 2

    while True:
        q = random_search(k - 1, t)
        # if q <= step:
        #    continue

        p = 2 * q + 1
        w = int((q - 1) / 2)

        if p in visited_naccache:
            continue

        if not division_with_primes_test(w):
            visited_naccache[w] = True
            visited_naccache[p] = True
            continue

        if division_with_primes_test(p) and miller_rabin(p, t):
            return p
        else:
            visited_naccache[p] = True


def naive_method_congruence(k, t=10):
    while True:
        q = random_search_congruence_sieve(k - 1, t)
        p = 2 * q + 1

        if p % 3 != 2:
            continue

        if division_with_primes_test(p) and miller_rabin(p, t):
            return p


def naive_method_small_primes(k, t=10):
    while True:
        q = random_search_small_primes_sieve(k - 1, t)

        p = 2 * q + 1

        if division_with_primes_test(p) and miller_rabin(p, t):
            return p


def naive_method_combined(k, t=10):
    while True:
        q = random_search_combined_sieves(k - 1, t)

        p = 2 * q + 1
        if p % 3 != 2:
            continue

        if division_with_primes_test(p) and miller_rabin(p, t):
            return p


def naive_method_combined_naccache(k, t=10):
    while True:
        q = random_search_combined_naccache(k - 1, t)

        p = 2 * q + 1
        if p % 3 != 2:
            continue

        if division_with_primes_test(p) and miller_rabin(p, t):
            return p