# kattis-accepted
f=lambda:map(int,input().split());n,m,*N=*f(),*f();print(sum(sum(1-x%2 for x in N[i:i+m])>1 for i in range(n-m+1)))
