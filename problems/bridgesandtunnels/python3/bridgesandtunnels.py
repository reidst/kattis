# kattis-accepted
buildings = dict()
N = int(input())
rank = [0 for i in range(2*N)]
uf = [i for i in range(2*N)]
sizes = [1 for i in range(2*N)]

def find(x):
    if uf[x] == x: return x
    return find(uf[x])
def union(u, v):
    ru, rv = find(u), find(v)
    newsize = sizes[ru] + sizes[rv]
    if ru != rv:
        if rank[ru] > rank[rv]:
            uf[rv] = ru
            sizes[ru] = newsize
        elif rank[ru] < rank[rv]:
            uf[ru] = rv
            sizes[rv] = newsize
        else:
            uf[ru] = rv
            sizes[rv] = newsize
            rank[rv] += 1

for i in range(N):
    l, r = input().split()
    if l not in buildings:
        buildings[l] = len(buildings)
    if r not in buildings:
        buildings[r] = len(buildings)
    union(buildings[l], buildings[r])
    print(sizes[find(buildings[l])])
