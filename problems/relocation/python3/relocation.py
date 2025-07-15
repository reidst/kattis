# kattis-accepted
N, Q = map(int, input().split())
loc = [0] + list(map(int, input().split()))
for _ in range(Q):
    i, x, y = map(int, input().split())
    if i == 1:
        loc[x] = y
    else:
        print(abs(loc[x] - loc[y]))

