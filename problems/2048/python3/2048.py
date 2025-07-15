# kattis-accepted
board = [list(map(int, input().split())) for _ in range(4)]
direction = int(input())


def swipe(b, d):
    if d in (1, 3):
        b = transpose(b)
    if d in (2, 3):
        for row in b:
            row.reverse()
    new_b = []
    for r in range(4):
        new_r = []
        squished = [n for n in b[r] if n != 0]
        can_combine = True
        for i, n in enumerate(squished):
            if i > 0 and n == new_r[-1] and can_combine:
                new_r[-1] *= 2
                can_combine = False
                continue
            new_r.append(n)
            can_combine = True
        new_r.extend([0] * (4 - len(new_r)))
        new_b.append(new_r)
    if d in (2, 3):
        for row in new_b:
            row.reverse()
    if d in (1, 3):
        new_b = transpose(new_b)
    return new_b


def transpose(b):
    new_b = [[None]*4 for _ in range(4)]
    for r, row in enumerate(b):
        for c, num in enumerate(row):
            new_b[c][r] = num
    return new_b


print(*(' '.join(map(str, row)) for row in swipe(board, direction)), sep='\n')
