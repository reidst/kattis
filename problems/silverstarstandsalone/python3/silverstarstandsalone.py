# kattis-accepted
distance = int(input())

def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if n%2 == 0 or n%3 == 0: return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0: return False
        i += 6
    return True

table = {2: 1}

for i in range(3, distance + 1):
    if not isprime(i): continue
    t = 0
    for j in table:
        if i - j > 14: continue
        t += table[j]
    table[i] = t

print(table[distance])
