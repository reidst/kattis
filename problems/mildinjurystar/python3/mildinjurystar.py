from collections import deque

rs,cs, n = map(int,input().split())

doors = {}

for i in range(n):
    inp = input().split()
    r = int(inp[0])
    c = int(inp[1])
    d = inp[2]
    t = int(inp[3])
    if d == 'S':
        doors[((r,c),(r+1,c))] = t
        doors[((r+1,c),(r,c))] = t
    else:
        doors[((r,c),(r,c+1))] = t
        doors[((r,c+1),(r,c))] = t

s = (0,0)
visited = set()
visited.add(s)
q = deque()
q.append(s)
levels = {}
levels[s] = 0
while q:
    u = q.popleft()
    for i in [(u[0]-1, u[1]), (u[0]+1,u[1]), (u[0], u[1]-1),(u[0],u[1]+1)]:
        if 0 <= i[0] < rs and 0 <= i[1] < cs and i not in visited and ((u,i) not in doors or levels[u] < doors[(u,i)]):
            levels[i] = levels[u] + 1
            q.append(i)
            visited.add(i)

dest = (rs-1,cs-1)
if dest in levels:
    print(levels[dest])
else:
    print("March he 30th be with you!")

                
