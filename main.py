from util import *
from tests import test_miller_rabin, stress_test_combined, stress_test_small_primes,\
    stress_test_congruence, stress_test_naccache, stress_test_naive


def main():
    compute_b(10000)

    LIMIT = 5000
    stress_test_naive(LIMIT)
    stress_test_congruence(LIMIT)
    stress_test_small_primes(LIMIT)
    stress_test_combined(LIMIT)


if __name__ == '__main__':
    main()
