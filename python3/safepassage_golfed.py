b=lambda x:4>len(x)and[max(x),sum(x)][len(x)>2]or min(x[0]*2+x[-2]+x[-1],x[0]+x[1]*2+x[-1])+b(x[:-2]);print(b(sorted(map(int,input().split()[1:]))))
