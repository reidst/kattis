# kattis-accepted
from itertools import permutations

def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if n%2 == 0 or n%3 == 0: return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0: return False
        i += 6
    return True

cases = int(input())
for case in range(cases):
    c = 0
    n = input()
    s = set()
    for count in range(len(n)):
        for perm in permutations(n, count + 1):
            new = int(''.join(perm))
            if new in s:
                continue
            if isprime(new):
                c += 1
            s.add(new)
    print(c)
