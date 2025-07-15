# kattis-accepted
def main():
    h, w, s = map(int, input().split())
    c = 1
    for _ in range(h):
        c += input().count('.')
    c *= s
    print(f'Your destination will arrive in {c} meters')


if __name__ == "__main__":
    main()
