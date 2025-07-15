# kattis-accepted
from collections import deque
from math import log


def main():
    num_gears = int(input())
    gears = dict()
    for _ in range(num_gears):
        size, count = map(int, input().split())
        if size in gears:
            gears[size].append(count)
        else:
            gears[size] = [count]
    prod = []
    for size in gears:
        counts = deque(sorted(gears[size]))
        while len(counts) > 1:
            big = counts.pop()
            small = counts.popleft()
            prod.append(big / small)
    print(sum(map(log, prod)))


if __name__ == "__main__":
    main()
