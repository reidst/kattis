# kattis-accepted
class UnionFind:
    def __init__(self, owes: list[int]):
        self.size: int = len(owes)
        self.arr: list[int] = [(i, o) for (i, o) in enumerate(owes)]
        self.depth: list[int] = [0 for _ in owes]

    def find(self, u: int) -> tuple[int, int]:
        if u < 0 or u >= self.size:
            raise ValueError(f'element {u} out of bounds for UnionFind of size {self.size}')
        while u != self.arr[u][0]:
            u = self.arr[u][0]
        return self.arr[u]

    def connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)

    def union(self, u: int, v: int) -> None:
        rui, ruo = self.find(u)
        rvi, rvo = self.find(v)
        if rui == rvi:
            return
        combined = ruo + rvo
        if self.depth[rui] < self.depth[rvi]:
            self.arr[rui] = (rvi, ruo)
            self.arr[rvi] = (rvi, combined)
            return
        if self.depth[rui] == self.depth[rvi]:
            self.depth[rui] += 1
        self.arr[rvi] = (rui, rvo)
        self.arr[rui] = (rui, combined)


def main():
    v, e = map(int, input().split())
    o = [int(input()) for _ in range(v)]
    uf = UnionFind(o)
    for _ in range(e):
        x, y = map(int, input().split())
        uf.union(x, y)
    if all(map(lambda x: uf.find(x[0])[1] == 0, uf.arr)):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
