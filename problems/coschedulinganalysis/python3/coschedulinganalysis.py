# kattis-accepted
import heapq

threads = int(input())

pq = []

for i in range(0, threads):
    intervals, *line = map(int, input().split())
    for i in range(0, intervals):
        heapq.heappush(pq, (line[2*i+1], -1))
        heapq.heappush(pq, (line[2*i], 1))

total = 0

last = -1

active = 0

while len(pq) != 0:
    time, val = heapq.heappop(pq)
    active += val

    if active >= 2 and last == -1:
        last = time

    if active < 2 and last != -1:
        total += (time - last)
        last = -1

    # print(val)

print(total)
