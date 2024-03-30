N = int(input())
p = 0
g = 0
pg = 1
for instruction in range(N):
    food, dist = input().split()
    dist = int(dist)
    if food == "P" and p < g and p + dist >= g:
        pg += 1
    elif food == "G" and g < p:
        pg += min(p - g, dist)
    if food == "P":
        p += dist
    elif food == "G":
        g += dist
print(pg)
