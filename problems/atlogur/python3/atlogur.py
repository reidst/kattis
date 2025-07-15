# kattis-accepted
n = int(input())
k = 0
h = 0
s = 0
for i in range(n):
    hj,sj = map(int,input().split())
    if k == 0:
        k = 1
        h = hj
        s = sj
    elif (h + sj -1)//sj >= (hj + s - 1)//s:
        h = h-(sj*(((hj + s - 1)//s)-1))
    else:
        k = i+1
        h = hj - (s*((h + sj -1)//sj))
        s = sj
print(k)
