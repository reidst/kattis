# kattis-accepted
from bisect import bisect_left

A = int(input())
names = [input() for _ in range(A)]
names.sort()

B = int(input())
for _ in range(B):
    nick = input()
    i = bisect_left(names, nick)
    j = list(nick)
    j[-1] = chr(1 + ord(j[-1]))
    j = ''.join(j)
    j = bisect_left(names, j)
    print(j - i)
