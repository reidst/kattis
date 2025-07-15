# kattis-accepted
def distance(a, b):
    if len(a) != len(b):
        return None
    return len(list(filter(lambda pair: pair[0] != pair[1], zip(a, b))))


def main():
    name = input()
    count = int(input())
    names = []
    for _ in range(count):
        names.append(input())
    distances = [distance(name, n) for n in names]
    for (i, n) in enumerate(distances):
        if n is not None and n <= 1:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
