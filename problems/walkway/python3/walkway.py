# kattis-accepted
# Written by Mark Johnson

def dijkstra(G, weight, s):
    d = {}
    q = set()
    for vertex in G:
        d[vertex] = 99999999999
    d[s] = 0
    q.add((d[s], s))
    while len(q) > 0:
        val, u = min(q)
        q.remove((val, u))
        if u not in G:
            continue
        for v in G[u]:
            if d[u] + weight[(u, v)] < d[v]:
                q.discard((d[v], v)) # Discard removes if nothing is there
                d[v] = weight[(u, v)] + d[u]
                q.add((d[v], v))
    return d

def main():
    num_stones = 1
    while num_stones != 0:
        num_stones = int(input())
        if num_stones == 0:
            break
        G = {}
        weight = {}
        for i in range(num_stones):
            a, b, h = map(int, input().split())
            area = (a+b)/2 * h
            if (a, b) not in weight:
                weight[(a, b)] = area
            else:
                if weight[(a, b)] > (a+b)/2 * h:
                    weight[(a, b)] = (a + b) / 2 * h
            if (b, a) not in weight:
                weight[(b, a)] = (a + b) / 2 * h
            else:
                if weight[(b, a)] > (a + b) / 2 * h:
                    weight[(b, a)] = (a + b) / 2 * h
            if a not in G:
                G[a] = [b]
            else:
                G[a].append(b)
            if b not in G:
                G[b] = [a]
            else:
                G[b].append(a)
        start, end = map(int, input().split())
        if start == end:
            print(0.00)
        else:
            d = dijkstra(G, weight, start)
            print(d[end] * .02)

main()
