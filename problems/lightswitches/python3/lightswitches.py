m, n = map(int, input().split())
input()
banks = [0 for _ in range(m)]
for b in range(m):
    switches = map(int, input().split())
    for s in switches:
        banks[b] ^= 1 << s
input()
ans = 0
ans_nums = list(map(int, input().split()))
for num in reversed(ans_nums):
    ans = ans * 2 + num

count = 0
for subs in range(2**m):
    x = 0
    for i in range(16):
        if subs & (1 << i) != 0:
            x ^= banks[i]
    if x == ans:
        count += 1

print(count)
