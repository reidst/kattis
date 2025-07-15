# kattis-accepted
shipw, shiph = map(int, input().split())
n, m = map(int, input().split())
asteroids = []
for _ in range(n):
    x, y, r = map(int, input().split())
    asteroids.append((x, y, r))

def intersect(shipx, shipy, asteroid):
    ax, ay, ar = asteroid
    # in bottomleft corner?
    bottomleft = (shipx - ax)**2 + (shipy - ay)**2 <= ar**2
    # in bottomright corner?
    bottomright = (shipx + shipw - ax)**2 + (shipy - ay)**2 <= ar**2
    # in topleft corner?
    topleft = (shipx - ax)**2 + (shipy + shiph - ay)**2 <= ar**2
    # in topright corner?
    topright = (shipx + shipw - ax)**2 + (shipy + shiph - ay)**2 <= ar**2
    # in vertical rect?
    vertical = (shipx <= ax <= (shipx + shipw)) and ((shipy - ar) <= ay <= (shipy + shiph + ar))
    # in horizontal rect?
    horizontal = ((shipx - ar) <= ax <= (shipx + shipw + ar)) and (shipy <= ay <= (shipy + shiph))
    return bottomleft or bottomright or topleft or topright or vertical or horizontal

for _ in range(m):
    x, y = map(int, input().split())
    if any(intersect(x, y, a) for a in asteroids):
        print("DOOMSLUG STOP!")
    else:
        print("DOOMSLUG GO!")
