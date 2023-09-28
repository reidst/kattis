from math import sqrt, ceil
from sys import stdin
input = stdin.readline
N, Q = map(int, input().split())
S = ceil(sqrt(N))
arr = [0 for _ in range(N+1)]
mods = [[0 for a in range(S)] for b in range(S)]

for query in range(Q):
    T, *args = map(int, input().split())
    if T == 1:
        A, B, C = args
        if B >= S:
            for k in range(A, N+1, B):
                arr[k] += C
        else:
            mods[B][A] += C
    else:
        D = args[0]
        total = arr[D] + sum(mods[b][D % b] for b in range(1, S))
        print(total)
