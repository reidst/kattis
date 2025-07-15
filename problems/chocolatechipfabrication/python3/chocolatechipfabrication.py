# kattis-accepted
from collections import deque

def iter_neighbors(loc):
    yield (loc[0] + 1, loc[1])
    yield (loc[0], loc[1] + 1)
    yield (loc[0] - 1, loc[1])
    yield (loc[0], loc[1] - 1)

height, width = map(int, input().split())
G = [[-1 for _ in range(width)] for _ in range(height)]
Q = deque()
m = 0
for row in range(height):
    for col, c in enumerate(input()):
        if c == '-':
            G[row][col] = 0
            Q.append((row,col))
for i in range(height):
    if G[i][0] == -1:
        G[i][0] = 1
        Q.append((i,0))
        m = 1
    if G[i][width-1] == -1:
        G[i][width-1] = 1
        Q.append((i,width-1))
        m = 1
for i in range(width):
    if G[0][i] == -1:
        G[0][i] = 1
        Q.append((0,i))
        m = 1
    if G[height-1][i] == -1:
        G[height-1][i] = 1
        Q.append((height-1,i))
        m = 1
while len(Q) > 0:
    spot = Q.popleft()
    count = G[spot[0]][spot[1]]
    for n in iter_neighbors(spot):
        row, col = n
        if row >= 0 and col >= 0 and row < height and col < width and G[row][col] == -1:
            G[row][col] = count + 1
            if count + 1 > m: m = count + 1
            Q.append(n)
print(m)
