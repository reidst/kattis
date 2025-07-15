# kattis-accepted
def main():
    n, p = map(int, input().split())
    t = []
    for _ in range(n):
        t.append(int(input()))
    num_decreasing = 0
    prev = None
    for i in t:
        if prev is not None and i < prev:
            num_decreasing += 1
        prev = i
    if t[0] == 0:
        for _ in range(n):
            print(0)
        return
    if t[-1] == 0:
        if num_decreasing < p:
            print("ambiguous")
            return
    else:
        if num_decreasing + 1 < p:
            print("ambiguous")
            return
    s = p
    prev = None
    for i in t:
        if prev is not None and i < prev:
            s -= 1
        print(s)
        prev = i


if __name__ == "__main__":
    main()
