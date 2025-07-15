# kattis-accepted
def main():
    h, w = map(int, input().split())
    iron = []
    for _ in range(h):
        for chr in input():
            iron.append(chr == "I")
    memo = [None] * h * w
    memo[h * w - 1] = iron[h * w - 1]
    for i in range(h * w - 2, -1, -1):
        r = i // w
        c = i % w
        if c + 1 == w:
            memo[i] = iron[i] + memo[i + w]
        elif r + 1 == h:
            memo[i] = iron[i] + memo[i + 1]
        else:
            memo[i] = iron[i] + max(memo[i + w], memo[i + 1])
    print(memo[0])


if __name__ == "__main__":
    main()
