# kattis-wa
from math import ceil, gcd, sqrt


def main():
    bx, by = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    bgcd = gcd(bx, by)
    if bgcd == 1:
        print("Yes")
    fx = bx // bgcd
    fy = by // bgcd
    lx = bx - fx
    ly = by - fy
    if x1 <= fx and y1 <= fy and lx <= x2 and ly <= y2:
        print("Yes")
        return
    print("No")
    slope = fy / fx
    int_horiz = y1 / slope
    dist_horiz = sqrt(y1 * y1 + int_horiz * int_horiz)
    int_vert = slope * x1
    dist_vert = sqrt(x1 * x1 + int_vert * int_vert)
    dist_int = max(dist_horiz, dist_vert)
    dist_first = sqrt(fx * fx + fy * fy)
    if dist_int > dist_first:
        print(fx, fy)
        return
    int_horiz2 = y2 / slope
    dist_horiz2 = sqrt(y2 * y2 + int_horiz2 * int_horiz2)
    int_vert2 = slope * x2
    dist_vert2 = sqrt(x2 * x2 + int_vert2 * int_vert2)
    dist_int2 = min(dist_horiz2, dist_vert2)
    ratio = dist_int2 / dist_first
    next_hit = ceil(ratio)
    hx = fx * next_hit
    hy = fy * next_hit
    print(hx, hy)


if __name__ == "__main__":
    main()
