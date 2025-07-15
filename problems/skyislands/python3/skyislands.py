# kattis-accepted
def find(uf, x):
    if uf[x] == x:
        return x
    return find(uf, uf[x])


def union(uf, sizes, rank, u, v):
    ru, rv = find(uf, u), find(uf, v)
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


def main():
    n, m = map(int, input().split())
    sizes = [1 for _ in range(n)]
    rank = [0 for _ in range(n)]
    uf = [*range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        union(uf, sizes, rank, a, b)
    p = (find(uf, i) for i in range(n))
    if len(set(p)) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
