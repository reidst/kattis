r, c, g = map(int, input().split())
gap = r + c - 1 - g
flips = set(range(0 if gap % 2 else 1, gap, 2))
for col in range(c):
    for row in range(r):
        diag = col + row
        print('/' if diag in flips else '\\', end='')
    print()
