# kattis-accepted
from collections import Counter


def main():
    ranks = map(lambda card: card[0], input().split())
    c = Counter(ranks)
    print(c.most_common(1)[0][1])


if __name__ == "__main__":
    main()
