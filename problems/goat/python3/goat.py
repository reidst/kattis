import math


def dot(p1, p2):
    return p1[0]*p2[0] + p1[1]*p2[1]


def mag(p):
    return math.sqrt(p[0]*p[0] + p[1]*p[1])


def angle(p1, p2):
    return math.acos(dot(p1, p2) / (mag(p1) * mag(p2)))


def det(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


r, n = map(float, input().split())
n = int(n)


points = []
total = 0

for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y))


d = []
for i in range(n):
    this = i
    that = (i + 1) % n
    d.append((points[that][0] - points[this][0], points[that][1] - points[this][1]))

# print(d)

p1 = (-r, 0)
p2 = d[0]
rad = angle(p1, p2)
if det(p1, p2) < 0:
    rad = math.pi - rad

# print(rad / (2*math.pi) * 360)
# print(f"{rad * r}, {r}")
total += rad * r
r -= mag(p2)


i = 0
while r > 0:
    this = i
    that = (i + 1) % n

    p1 = d[this]
    p2 = d[that]

    rad = angle(p1, p2)
    if det(p1, p2) < 0:
        rad = math.pi - rad

    # print(rad / (2*math.pi) * 360)
    # print(f"{rad * r}, {r}")
    total += rad * r
    r -= mag(p2)

    i = (i + 1) % n

print(total)
