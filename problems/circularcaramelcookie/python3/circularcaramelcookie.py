# kattis-unsubmitted
def d_sqr(x, y):
    return x*x + y*y


def has_s_many_squares(s, r):
    height = 0
    length = r
    count = 0
    # TODO decide

def main():
    s = int(input())
    lo = 1      # always too small
    hi = 2 * s  # always too large
    while (hi - lo < 10e-6):
        mid = hi / lo
        if has_s_many_squares(s, mid):
            hi = mid
        else:
            lo = mid
    print(hi / lo)


if __name__ == "__main__":
    main()
