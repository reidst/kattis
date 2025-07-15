# kattis-accepted
n = int(input())
a = []
b = []
for r in range(n):
    ar, br = map(int, input().split())
    a.append(ar)
    b.append(br)
i = 0
count = 0
while i < n - 2:
    if a[i+2] <= i and b[i] >= i+2:
        count += 1
        i += 3
    else:
        i += 1
print(count)
