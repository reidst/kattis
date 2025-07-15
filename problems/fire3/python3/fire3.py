# kattis-tle
from collections import deque
def neighbors(pos):
    nc,nr = pos
    return ((nc,nr+1), (nc,nr-1), (nc+1,nr), (nc-1,nr))
r, c = map(int, input().split())
G = {}
fire_time = {}
joe_time = {}
fq = deque()
jq = deque()
for row in range(r):
    text_row = input()
    for col in range(c):
        loc = (col, row)
        cell = text_row[col]
        G[loc] = cell
        if cell == 'F':
            fire_time[loc] = 0
            fq.append(loc)
        if cell == 'J':
            joe_time[loc] = 0
            jq.append(loc)
while len(fq) > 0:
    pos = fq.popleft()
    val = fire_time[pos]
    for neighbor in neighbors(pos):
        if G.get(neighbor, '#') == '#':
            continue
        if neighbor in fire_time:
            continue
        fire_time[neighbor] = val + 1
        fq.append(neighbor)
while len(jq) > 0:
    pos = jq.popleft()
    val = joe_time[pos]
    for neighbor in neighbors(pos):
        if G.get(neighbor, '#') == '#':
            continue
        if neighbor in joe_time:
            continue
        if neighbor in fire_time and fire_time[neighbor] <= val + 1:
            continue
        joe_time[neighbor] = val + 1
        jq.append(neighbor)
def edges():
    return (
        *((i,0) for i in range(c)),
        *((i,r-1) for i in range(c)),
        *((0,i) for i in range(1,r-1)),
        *((c-1,i) for i in range(1,r-1))
    )
finish_time = None
for edge in edges():
    this_time = joe_time.get(edge, None)
    if this_time is not None:
        if finish_time is None or this_time < finish_time:
            finish_time = this_time
print(finish_time + 1 if finish_time is not None else "IMPOSSIBLE")
