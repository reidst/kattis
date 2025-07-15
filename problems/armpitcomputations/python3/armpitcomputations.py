# kattis-tle
from collections import deque

mask = 2**13 - 1

def ORWITH(v,i):
    return v | i

def LSL(v,i):
    return (v << i) & mask

def ROR(v,i):
    return ((v & 1) << 11) | (v >> 1)

def ADDSHIFT(v,i):
    v1 = v
    return (v1 + LSL(v,i)) & mask

def ADDONE(x):
    return (x + 1) & mask

def NOT(x):
    return (~x) & mask

def dist(x):
    q = deque()
    q.append(0)
    vis = set()
    p = {}
    p[0] = 0
    level = {}
    level[0] = 0
    
    while len(q) != 0:
        v = q.popleft()
        #print(f"{v} + {level[v]}")

        if v == x:
            return level[v]
        next = set()
        for i in range(16):
            next.add(ORWITH(v,i))
        for i in range(8):
            next.add(LSL(v,i))
            next.add(ROR(v,i))
            next.add(ADDSHIFT(v,i))
        next.add(ADDONE(v))
        next.add(NOT(v))

        #print(next)

        next_level = level[v] + 1
        for u in next:
            if u not in vis:
                p[u] = v
                level[u] = next_level
                vis.add(u)
                q.append(u)

        


n = int(input())
xs = []

for i in range(n):
    x = int(input())
    print(dist(x))


