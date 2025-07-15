# kattis-accepted
mod = 1000000007

def modexp(base, pow, modulus):
    if pow == 0: return 1
    
    i = modexp(base, pow//2, modulus)
    if pow%2 == 0: # even
        return (i * i) % modulus
    else: # odd
        return (i * i * base) % modulus


def main():
    num_tests = int(input())
    for test in range(num_tests):
        d = int(input())
        print((8 * modexp(9, d-1, mod)) % mod)



if __name__ == '__main__':
    main()