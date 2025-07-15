# kattis-accepted
height, width = map(int, input().split())
dots = set()
letters = set()
list_grid = []
graph_grid = {} # key = coord, val = letter
G = {} # key = coord, val = list of neighbors
visited = set()

for row in range(height):
    line = input()
    list_grid.append(list(line))

    for col in range(width):
        if line[col] == '.':
            dots.add((row, col))
        if line[col] not in ('X', ' ', '.'):
            letters.add((row, col))

for row in range(height):
    for col in range(width):
        graph_grid[(row, col)] = list_grid[row][col]

for pos in graph_grid:
    if graph_grid[pos] == 'X':
        continue
    valid_neighbors = []
    for neighbor in ((pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)):
        if neighbor in graph_grid and graph_grid[neighbor] in (' ', '.'):
            valid_neighbors.append(neighbor)
    G[pos] = valid_neighbors

total_dots = len(dots)

def bfs(start):
    global total_dots, graph_grid, G, visited
    found_dot = False
    Q = []
    Q.append(start)
    visited.add(start)
    while len(Q) > 0:
        u = Q.pop(0)
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                Q.append(v)
                if graph_grid[v] == '.':
                    graph_grid[v] = ' '
                    total_dots -= 1
                    found_dot = True
    return found_dot

players = 0
for start in letters:
    if bfs(start):
        players += 1

print(players, total_dots)
