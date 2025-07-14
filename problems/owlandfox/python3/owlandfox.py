# kattis-unsolved
def main():
    for _ in range(int(input())):
        x = int(input())
        y = 1
        while x % y == 0:
            y *= 10
        y //= 10
        print(x-y)


if __name__ == "__main__":
    main()
