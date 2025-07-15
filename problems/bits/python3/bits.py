# kattis-accepted
N = int(input())
for i in range(N):
    num = input()
    build = ''
    counts = []
    for digit in num:
        build += digit
        counts.append(bin(int(build)).count('1'))
    print(max(counts))
