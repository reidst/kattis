# kattis-accepted
def mat_mul(a, b, m):
    return [ [ (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
             , (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m ]
           , [ (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
             , (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m ] ]


def fast_exp(mat, pow, m):
    if pow == 0:
        return [[1, 0], [0, 1]]
    elif pow % 2 == 0:
        split_mat = fast_exp(mat, pow // 2, m)
        return mat_mul(split_mat, split_mat, m)
    else:
        split_mat = fast_exp(mat, pow // 2, m)
        comb_mat = mat_mul(split_mat, split_mat, m)
        return mat_mul(mat, comb_mat, m)


def main():
    a, b, x0, n, m = map(int, input().split())
    f = [[a, b], [0, 1]]
    fn = fast_exp(f, n, m)
    print((fn[0][0] * x0 + fn[0][1]) % m)


if __name__ == "__main__":
    main()
