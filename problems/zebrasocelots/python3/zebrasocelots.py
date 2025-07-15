# kattis-accepted
N = int(input())
total = 0
for i in range(N):
    animal = input().lower()
    if animal == 'z':
        total = total * 2
    else:
        total = total * 2 + 1
print(total)
