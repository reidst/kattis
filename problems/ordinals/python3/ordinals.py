# kattis-accepted
def f(i):return"{"+','.join(map(f,range(i)))+"}"
print(f(int(input())))
