# kattis-accepted
for n in map(input,' '*int(input())):print(sum(map(lambda p:False if p<2 else True if p<4 else False if p%2==0 or p%3==0 else False if any(map(lambda x:p%x==0 or p%(x+2)==0,range(5,int(p**0.5)+1,6)))else True,set(map(lambda r:int(''.join(r)),(r for c in range(len(n))for r in __import__('itertools').permutations(n,c+1)))))))
