# kattis-accepted
l = int(input())
d = int(input())
x = int(input())
for i in range(l, d+1):
    digitsum = sum(map(int, str(i)))
    if digitsum == x:
        print(i)
        break
for i in range(d, l-1, -1):
    digitsum = sum(map(int, str(i)))
    if digitsum == x:
        print(i)
        break