import math

# from geeksforgeeks

# Function to find modulo inverse of b. It returns 
# -1 when inverse doesn't 
# modInverse works for prime m
def modInverse(b,m):
    g = math.gcd(b, m) 
    if (g != 1):
        # print("Inverse doesn't exist") 
        return -1
    else: 
        # If b and m are relatively prime, 
        # then modulo inverse is b^(m-2) mode m 
        return pow(b, m - 2, m)
 
 
# Function to compute a/b under modulo m 
def modDivide(a,b,m):
    a = a % m
    inv = modInverse(b,m)
    return (inv*a) % m


n, k = map(int, input().split())

MOD = (10**9 + 7)


def fac_mod(num):
    ans = 1
    for i in range(2, num+1):
        ans = (ans * i) % MOD
    return ans


if n % k == 0:
    s = n // k
    ans = modDivide(fac_mod(n),fac_mod(s)*(fac_mod(k)**s), MOD)
    print(ans)
else:
    print(0)




