# kattis-accepted
_ = input()
P = float(input())
D = int(input())
N = 0
for i in range(D):
    if input() == 'ekki plast':
        N += 1
if N/D > P:
    print('Neibb')
else:
    print('Jebb')
