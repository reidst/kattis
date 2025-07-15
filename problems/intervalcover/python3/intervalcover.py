# kattis-unsubmitted
def test_case(A, B):
    interval_count = int(input())
    intervals = list()
    for i in range(interval_count):
        intervals.append((*map(float, input().split()), i))
    # sort intervals by lower bound
    # track the lower bound needed to cover
    # iterate over intervals, tracking rightmost endpoint
    # once an interval with lower bound right of the needed lower bound is reached, select the rightmost-tracked interval
    # update tracked lower bound and repeat process
    chosen = set()
    intervals.sort()
    left = A
    i = 0
    while left < B and i < interval_count:
        rightmost = left
        rightmost_i = -1
        while i < interval_count and intervals[i][0] <= left:
            if intervals[i][1] >= rightmost:
                rightmost = intervals[i][2]
                rightmost_i = i
            i += 1
        chosen.add(rightmost_i)
        left = rightmost
    if left >= B:
        print(len(chosen))
        print(*chosen)
    else:
        print("impossible")

from sys import stdin
base = stdin.readline()
while base:
    A, B = map(float, base.split())
    test_case(A, B)
