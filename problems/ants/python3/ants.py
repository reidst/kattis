# kattis-accepted
def main():
    num_cases = int(input())
    for case in range(num_cases):
        length, num_ants = map(int, input().split())
        ants = []
        while len(ants) < num_ants:
            ants.extend(map(int, input().split()))
        ants.sort()
        solve(ants, length)


def solve(ants, length):
    shortest = 0
    for ant in ants:
        dist = min(ant, length - ant)
        shortest = max(shortest, dist)
    longest = 0
    for ant in ants:
        dist = max(ant, length - ant)
        longest = max(longest, dist)
    print(shortest, longest)


if __name__ == "__main__":
    main()
