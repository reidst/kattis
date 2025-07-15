# kattis-accepted
from math import ceil
def f(n, b, ans=1):
    if n <= 1:
        return ans
    elif n <= b:
        return ans
    else:
        n = ceil((n - b) / (b + 1))
        return f(n, b, ans+1)
n, b = map(int, input().split())
print(f(n, b))
