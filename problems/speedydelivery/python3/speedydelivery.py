def dijkstra(G, weight, s):
    d = {}
    parent = {s: s}
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
                parent[v] = u
                q.discard((d[v], v))
                d[v] = weight[(u, v)] + d[u]
                q.add((d[v], v))
    return d, parent


n, s, p, d, k = map(int, input().split())
G = {}
weights = {}
for _ in range(k):
    i, j, t = map(int, input().split())
    if i not in G:
        G[i] = [j]
    else:
        G[i].append(j)
    if j not in G:
        G[j] = [i]
    else:
        G[j].append(i)
    weights[(i, j)] = t
    weights[(j, i)] = t

d_s, p_s = dijkstra(G, weights, s)
s_p_path = set()
tmp = p
while p_s[tmp] != tmp:
    s_p_path.add(tmp)
    tmp = p_s[tmp]
s_p_path.add(s)

d_d, p_d = dijkstra(G, weights, d)
minimum = 999999999999999
for s_p_point in s_p_path:
    if s_p_point in d_d and d_d[s_p_point] < minimum:
        minimum = d_d[s_p_point]

print(d_s[p] + minimum)
