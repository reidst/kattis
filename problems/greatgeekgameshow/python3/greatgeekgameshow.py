# kattis-unsubmitted
import random


# the boxes form a graph of C number of cyclical components
# if player N starts at box N, their number is at the end of the cycle
#   always in the cycle they start at
# essentially:
#   what is the probability that a number falls within a cycle of length <= K?
def simulate(n, k):
    wins = 0
    amt = 1_000_000
    for round in range(amt):
        lst = list(range(n))
        random.shuffle(lst)
        failed = False
        for person in range(n):
            choice = person
            found = False
            for _ in range(k):
                box = lst[choice]
                if box != person:
                    choice = box
                else:
                    found = True
                    break
            if not found:
                failed = True
                break
        if not failed:
            wins += 1
    print(wins / amt)


def main():
    n, k = map(int, input().split())
    simulate(n, k)


if __name__ == "__main__":
    main()
