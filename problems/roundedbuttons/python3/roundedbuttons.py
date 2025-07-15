# kattis-accepted
n = int(input())
def colliderect(x, y, w, h, px, py):
    return px >= x and px <= x + w and py >= y and py <= y + h
def collidecircle(x, y, r, px, py):
    return ((px - x)**2 + (py - y)**2 <= r**2)
for _ in range(n):
    x, y, w, h, r, m, *points = map(float, input().split())
    for p in range(int(m)):
        px = points[2*p]
        py = points[2*p + 1]
        if colliderect(x+r, y, w-2*r, h, px, py) \
            or colliderect(x, y+r, w, h-2*r, px, py) \
            or collidecircle(x+r, y+r, r, px, py) \
            or collidecircle(x+w-r, y+r, r, px, py) \
            or collidecircle(x+w-r, y+h-r, r, px, py) \
            or collidecircle(x+r, y+h-r, r, px, py):
            print("inside")
        else:
            print("outside")