# kattis-accepted
from math import gcd, sqrt
from functools import reduce


def smallest_factor(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x


def prime_factors(x):
    if x == 1:
        return []
    else:
        sf = smallest_factor(x)
        k = x
        c = 0
        while k % sf == 0:
            k //= sf
            c += 1
        return prime_factors(k) + [(sf, c)]


def flatmap(lam, l):
    return sum([lam(x) for x in l], [])


def powermultiset(l):
    if len(l) == 0:
        return [[]]
    else:
        (h, c), *t = l
        tp = powermultiset(t)
        return flatmap(lambda x: [[*x, *([h] * i)] for i in range(c+1)], tp)


def divisors(x):
    prod = lambda l: reduce(int.__mul__, l, 1)
    return filter(lambda x: x > 1, map(prod, powermultiset(prime_factors(x))))


# 2 <= N <= 100
# 1 <= x_n <= 1_000_000_000
def main():
    count = int(input())
    nums = sorted([int(input()) for _ in range(count)])
    diffs = []
    for (i, a) in enumerate(nums):
        for b in nums[i+1:]:
            diffs.append(abs(a-b))
    g = reduce(gcd, diffs, 0)
    print(*filter(lambda x: x > 1, divisors(g)), sep=' ')


if __name__ == "__main__":
    main()
