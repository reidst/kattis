# kattis-accepted
from math import floor, log
def sevens_in_range(limit):
    if limit < 10:
        return 0 if limit < 7 else 1
    scale = 10**floor(log(limit, 10))
    first_digit = limit // scale
    other_digits = limit % scale
    if first_digit < 7:
        return sevens_in_range(scale - 1) * first_digit + sevens_in_range(other_digits)
    elif first_digit == 7:
        return sevens_in_range(scale - 1) * first_digit + other_digits + 1
    else:
        return sevens_in_range(scale - 1) * (first_digit - 1) + scale + sevens_in_range(other_digits)
lo, hi = map(int, input().split())
print(sevens_in_range(hi) - sevens_in_range(lo-1))
