# kattis-accepted
from math import pi, tau, sin


def fits(target_diameter, side_len, count):
    # sin(A)/a = sin(B)/b
    # sin(angle)/side_len = sin(half_interior_angle)/b
    # b = side_len * sin(half_interior_angle) / sin(angle)
    angle = tau / count
    half_interior_angle = (pi - angle) / 2
    shape_diameter = 2 * side_len * sin(half_interior_angle) / sin(angle)
    return shape_diameter <= target_diameter


def solve(D, d, s):
    diameter_check = D - d
    side = d + s
    guarantee = 3
    try_size = 3
    while fits(diameter_check, side, try_size):
        guarantee = try_size
        try_size *= 2
    lo = guarantee
    hi = try_size
    while hi - lo > 1:
        mid = (hi - lo) // 2 + lo
        if fits(diameter_check, side, mid):
            lo = mid
        else:
            hi = mid
    return lo


def main():
    for _ in range(int(input())):
        D, d, s = map(float, input().split())
        print(solve(D, d, s))


if __name__ == "__main__":
    main()