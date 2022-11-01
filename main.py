import math


def main():
    n = 630
    for n in range(132):
        factors = get_prime_factors(n)
        if factors:
            product = math.prod(factors)
            assert product == n, f'{product} != {n}'
            print(f'{n}: Prime factors: {factors}, product: {product}')
        else:
            print(f'{n}: No prime factors found.')


def get_prime_factors(num: int) -> list:
    factors = []
    # shortcut for primes
    if is_prime(num):
        return [num]

    for factor in range(2, num):
        if is_prime(factor):
            while num % factor == 0:
                factors.append(factor)
                num /= factor

    return factors


def is_prime(num: int) -> bool:
    """

    Args:
        num ():

    Returns:

    """
    if num < 2:
        return False

    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
