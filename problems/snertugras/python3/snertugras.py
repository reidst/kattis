#kattis-accepted
from collections import deque


def solve_no_walls(start, end):
    m = None
    for e in end:
        d = abs(e[0] - start[0]) + abs(e[1] - start[1])
        if m is None or d < m:
            m = d
    print(m)


def solve_bfs(start, end, open):
    q = deque()
    q.append((start, 0))
    while len(q) > 0:
        (v, vdist) = q.popleft()
        if v in end:
            print(vdist)
            return
        for delta in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            dv = (v[0] + delta[0], v[1] + delta[1])
            if dv in open:
                q.append((dv, vdist + 1))
                open.remove(dv)
    print("thralatlega nettengdur")


def main():
    h, w = map(int, input().split())
    open = set()
    start = None
    end = set()
    no_walls = True
    for r in range(h):
        line = input()
        for c in range(w):
            char = line[c]
            if char != "#":
                open.add((r, c))
            else:
                no_walls = False
            if char == "S":
                start = (r, c)
                open.remove(start)
            elif char == "G":
                end.add((r, c))
    if no_walls and len(end) > 0:
        solve_no_walls(start, end)
    else:
        solve_bfs(start, end, open)


if __name__ == "__main__":
    main()
