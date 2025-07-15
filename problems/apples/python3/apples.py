# kattis-accepted
R, C = map(int, input().split())

board = []
for r in range(R):
    row = []
    line = input()
    for c in range(C):
        row.append(line[c])
    board.append(row)
transposed = []
for c in range(C):
    col = []
    for r in range(R):
        col.append(board[r][c])
    transposed.append(col)

moved = []
for row in transposed:
    split_row = "".join(row).split("#")
    moved_row = map(lambda s: "".join(sorted(s)), split_row)
    moved.append("#".join(moved_row))

for r in range(R):
    for c in range(C):
        print(moved[c][r], end='')
    print()
