# kattis-accepted
def matrix_mul(mat_a, mat_b, modulus):
    a, b, c, d = mat_a
    e, f, g, h = mat_b
    return ((a*e + b*g) % modulus, (a*f + b*h) % modulus, (c*e + d*g) % modulus, (c*f + d*h) % modulus)

def matrix_modexp(mat, pow, modulus):
    if pow == 0:
        return (1, 0, 0, 1)
    elif pow == 1:
        return mat
    elif pow % 2 == 0:
        x = matrix_modexp(mat, pow // 2, modulus)
        return matrix_mul(x, x, modulus)
    else:
        x = matrix_modexp(mat, pow // 2, modulus)
        return matrix_mul(matrix_mul(x, x, modulus), mat, modulus)

num_datasets = int(input())
for dataset in range(num_datasets):
    k, y = map(int, input().split())
    fib_matrix = matrix_modexp((1, 1, 1, 0), y, 1_000_000_000)
    print(k, fib_matrix[1])
