# kattis-accepted
import math


def is_prime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if (x % 2 == 0) or (x % 3 == 0):
        return False
    i = 5
    while i*i < x:
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
        i += 6
    return True


def solve(s):
    max_ord = max(map(ord, s))
    cases = 1
    primes = 0
    if max_ord > 57:
        cases = 1
    elif max_ord >= 56:
        cases = 2
    elif max_ord >= 50:
        cases = 3
    else:
        cases = 4
    if cases >= 1 and is_prime(int(s, 16)):
        primes += 1
    if cases >= 2 and is_prime(int(s, 10)):
        primes += 1
    if cases >= 3 and is_prime(int(s, 8)):
        primes += 1
    if cases >= 4 and is_prime(int(s, 2)):
        primes += 1
    g = math.gcd(primes, cases)
    num = primes // g
    den = cases // g
    print(f"{num}/{den}")


def main():
    for _ in range(int(input())):
        solve(input())


if __name__ == "__main__":
    main()
