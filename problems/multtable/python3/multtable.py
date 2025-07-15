# kattis-partial
N, M = map(int, input().split())
c = 0
for i in range(1, N+1):
    if M % i == 0 and M / i <= N:
        c += 1
print(c)
