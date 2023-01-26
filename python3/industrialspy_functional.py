from itertools import permutations

def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if n%2 == 0 or n%3 == 0: return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0: return False
        i += 6
    return True

cases = int(input())
for case in range(cases):
    n = input()
    perms = (perm for count in range(len(n)) for perm in permutations(n, count + 1))
    perms = map(lambda perm: int(''.join(perm)), perms)
    unique_perms = set(perms)
    prime_count = sum(map(isprime, unique_perms))
    print(prime_count)

# a fun one-liner version:
# for n in map(input,' '*int(input())):print(sum(map(lambda p:False if p<2 else True if p<4 else False if p%2==0 or p%3==0 else False if any(map(lambda x:p%x==0 or p%(x+2)==0,range(5,int(p**0.5)+1,6)))else True,set(map(lambda r:int(''.join(r)),(r for c in range(len(n))for r in __import__('itertools').permutations(n,c+1)))))))
