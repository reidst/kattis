# kattis-accepted
def score(expected, actual):
    diff = abs(expected - actual)
    if diff <= 15:
        return 7
    if diff <= 23:
        return 6
    if diff <= 43:
        return 4
    if diff <= 102:
        return 2
    return 0


def main():
    num_expected, num_actual = map(int, input().split())
    expected = [int(input()) for _ in range(num_expected)]
    actual = [int(input()) for _ in range(num_actual)]
    # cases:
    # - expected[i] matches with actual[j], i++, j++
    # - expected[i] is skipped, i++
    # - actual[j] is skipped, j++
    table = [[None for _ in range(num_actual + 1)] for _ in range(num_expected + 1)]
    for i in range(num_expected, -1, -1):
        for j in range(num_actual, -1, -1):
            if i == num_expected or j == num_actual:
                table[i][j] = 0
                continue
            match = score(expected[i], actual[j]) + table[i + 1][j + 1]
            skip_expected = table[i + 1][j]
            skip_actual = table[i][j + 1]
            table[i][j] = max(match, skip_expected, skip_actual)
    print(table[0][0])


if __name__ == "__main__":
    main()
