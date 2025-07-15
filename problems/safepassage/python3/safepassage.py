# kattis-accepted
_,*a=map(int,input().split())
a.sort()

def b(x):
    if len(x) == 2:
        return max(x)
    elif len(x) == 3:
        return sum(x)
    else:
        return min(
            x[0]*2+x[-2]+x[-1],
            x[0]+x[1]*2+x[-1]
        )+b(x[:-2])

print(b(a))
