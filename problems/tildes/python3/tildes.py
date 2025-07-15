# kattis-tle
n, q = map(int, input().split())

p2g = [i for i in range(n)]
groups = [{i,} for i in range(n)]

for line in range(q):
    qtype, *args = input().split()
    args = map(lambda x: int(x)-1, args)
    if qtype == 's':
        a ,= args
        print(len(groups[p2g[a]]))
    elif qtype == 't':
        a, b = args
        groupa = groups[p2g[a]]
        groupb = groups[p2g[b]]
        if groupa == groupb: continue
        for p in groupb:
            p2g[p] = p2g[a]
        groupa.update(groupb)
        groupb.clear()
