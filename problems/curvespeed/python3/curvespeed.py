# kattis-accepted
from sys import stdin
from math import sqrt


def main():
    for line in stdin.readlines():
        r, s = line.split()
        r, s = int(r), float(s)
        v = sqrt((r * (s + .16)) / .067)
        print(round(v))


if __name__ == "__main__":
    main()
