from collections import deque

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

c = int(input())

G = {}

for i in range(1,c+1):
    G[i] = list(map(int,input().split()))[1:]

union = UnionFind(c)
checked = set()
for i in range(1,c+1):
    if i not in checked:
        checked.add(i)
        stack = deque()
        parent = {}
        visited = set()
        stack.append(i)
        parent[i] = i
        visited.add(i)
        while stack:
            u = stack.pop()
            for v in G[u]:
                if v in visited:
                    temp = parent[v]
                    while temp != v:
                        union.union(v,u)
                else:
                    stack.append(v)
                    visited.add(v)
                    checked.add(v)
                    parent[v] = u

print(max(union.sizes))
