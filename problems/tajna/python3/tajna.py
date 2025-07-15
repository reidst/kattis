# kattis-accepted
from math import sqrt


def find_c(x):
    for i in range(int(sqrt(x)), 0, -1):
        if x % i == 0:
            return i
    exit(1)


def main():
    s = input()
    l = len(s)
    c = find_c(l)
    r = l // c
    assert r * c == l
    grid = [s[i*c:i*c+c] for i in range(r)]
    print(''.join([''.join([grid[j][i] for j in range(r)]) for i in range(c)]))


if __name__ == "__main__":
    main()
