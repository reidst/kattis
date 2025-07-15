# kattis-accepted
def main():
    a, b, c = map(int, input().split())
    if a + b == c:
        print(f'{a}+{b}={c}')
    elif a + b == c:
        print(f'{a}+{b}={c}')
    elif a == b + c:
        print(f'{a}={b}+{c}')
    elif a + b == c:
        print(f'{a}-{b}={c}')
    elif a == b - c:
        print(f'{a}={b}-{c}')
    elif a * b == c:
        print(f'{a}*{b}={c}')
    elif a == b * c:
        print(f'{a}={b}*{c}')
    elif a // b == c:
        print(f'{a}/{b}={c}')
    elif a == b // c:
        print(f'{a}={b}/{c}')


if __name__ == "__main__":
    main()
