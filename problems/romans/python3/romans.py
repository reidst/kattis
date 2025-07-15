# kattis-accepted
def main():
    x = float(input())
    y = x / 4854 * 5280000
    if 2 * y == int(2 * y):
        print(int(y + 0.5))
    else:
        print(round(y))


if __name__ == "__main__":
    main()
