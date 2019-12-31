import time
from generators import naive_method, naive_method_small_primes, naive_method_congruence,\
    naive_method_naccache, naive_method_combined, naive_method_combined_naccache
from millerrabin import miller_rabin


def test_miller_rabin():
    t = [5, 7, 11, 23, 47, 59, 83, 107, 167, 221]
    for x in t:
        print('{}->{}'.format(x, miller_rabin(x, 4)))


def stress_test_naive(LIMIT, k=10):
    print('Testing naive method:')
    start = time.time()
    for i in range(LIMIT):
        naive_method(k)
    end = time.time()
    print('Time elapsed: {}\n'.format(end - start))


def stress_test_naccache(LIMIT, k=10):
    print('Testing naive method with Naccache:')
    start = time.time()
    for i in range(LIMIT):
        naive_method_naccache(k)
    end = time.time()
    print('Time elapsed: {}\n'.format(end - start))


def stress_test_congruence(LIMIT, k=10):
    print('Testing naive method with congruence filter:')
    start = time.time()
    for i in range(LIMIT):
        naive_method_congruence(k)
    end = time.time()
    print('Time elapsed: {}\n'.format(end - start))


def stress_test_small_primes(LIMIT, k=10):
    print('Testing naive method with small primes filter:')
    start = time.time()
    for i in range(LIMIT):
        naive_method_small_primes(k)
    end = time.time()
    print('Time elapsed: {}\n'.format(end - start))


def stress_test_combined(LIMIT, k=10):
    print('Testing naive method with combined sieves:')
    start = time.time()
    for i in range(LIMIT):
        naive_method_combined(k)
    end = time.time()
    print('Time elapsed: {}\n'.format(end - start))


def stress_test_combined_naccache(LIMIT, k=10):
    print('Testing naive method with combined sieves and using Naccache method:')
    start = time.time()
    for i in range(LIMIT):
        naive_method_combined_naccache(k)
    end = time.time()
    print('Time elapsed: {}\n'.format(end - start))
