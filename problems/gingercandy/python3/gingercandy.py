# kattis-unsolved
class UnionFind:
    def __init__(self, n: int):
        self.arr: list[int] = [i for i in range(n)]
        self.depth: list[int] = [0 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]
        self.size: int = n
        self.group_count: int = n

    def find(self, u: int) -> int:
        if u < 0 or u >= self.size:
            raise ValueError(f'element {u} out of bounds for UnionFind of size {self.size}')
        while u != self.arr[u]:
            u = self.arr[u]
        return u

    def connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)

    def union(self, u: int, v: int) -> None:
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            return
        self.group_count -= 1
        if self.depth[ru] < self.depth[rv]:
            self.sizes[rv] += self.sizes[ru]
            self.arr[ru] = rv
            return
        if self.depth[ru] == self.depth[rv]:
            self.depth[ru] += 1
        self.arr[rv] = ru


def main():
    n, m, a = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
    edges.sort(key=lambda p: p[2])
    g = dict()
    uf = UnionFind(n)
    for (u, v, c) in edges:
        if uf.connected(u, v):
            pass
            # use sum of length of BFS(g, u, v) + c
            # then print it
        else:
            uf.union(u, v)
            g[u].append((v, c))
            g[v].append((u, c))


if __name__ == "__main__":
    main()
