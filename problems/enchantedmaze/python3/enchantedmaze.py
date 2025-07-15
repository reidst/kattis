# kattis-unsubitted
from collections import deque


# bit order (LSB first):
# switches 1-4, kid (A (row, col), B (row, col))
def compactify(switches, kids):
    a, b = kids
    ar, ac = a
    br, bc = b
    # 4 bits
    switch_part = sum(v << i for (i, v) in enumerate(switches))
    # 8 bits
    a_part = ((ac & 15) << 4) + (ar & 15)
    # 8 bits
    b_part = ((bc & 15) << 4) + (br & 15)
    return (b_part << 12) + (a_part << 4) + switch_part


def decompactify(state):
    switch_part = state & 15
    state >>= 4
    a_part = state & 255
    state >>= 8
    b_part = state & 255
    switches = [(switch_part & (1 << i)) != 0 for i in range(4)]
    ar = a_part & 15
    ac = (a_part >> 4) & 15
    a = (ar, ac)
    br = b_part & 15
    bc = (b_part >> 4) & 15
    b = (br, bc)
    return (switches, (a, b))


def main():
    return
    R, C = map(int, input().split())
    # static information
    board = {}
    exits = []
    # information dependent on state
    switches = [False, False, False, False]
    kids = []
    # construct static information, pick up the kids
    for row in range(R):
        line = input()
        for (col, char) in enumerate(line):
            pos = (row, col)
            if char == "S":
                kids.append(pos)
            elif char == "E":
                exits.append(pos)
            else:
                board[pos] = char
    # BFS
    # TODO keep track of seconds
    q = deque()
    q.append(compactify(switches, kids))
    while len(q) > 0:
        state = q.popleft()
        # TODO find your neighbors in this dystopian suburbia of a neighborhood
        neighbors = find_neighbors(board, state)
        for n in neighbors:
            a, b = n[1]
            if a in exits and b in exits and a != b:
                # found it!
                pass


if __name__ == "__main__":
    main()
