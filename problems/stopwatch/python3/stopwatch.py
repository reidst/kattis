# kattis-accepted
N = int(input())
if N%2 != 0:
    print("still running")
else:
    c = 0
    for i in range(N//2):
        c += (abs(int(input()) - int(input())))
    print(c)