N = int(input())
h = dict()
for row in range(N):
    line = list(map(int, input().split()))
    for col in range(N):
        h[(col,row)] = line[col]
print(h)
