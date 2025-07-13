# kattis-unsolved
def main():
    n, l, t = map(int, input().split())
    max_keys = l * t
    words = input().split()
    for w in words:
        if len(w) + 1 > max_keys:
            print("/ff")
            return


if __name__ == "__main__":
    main()
