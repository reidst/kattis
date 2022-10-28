from bisect import*;l=bisect_left;i=input;e=sorted(map(i,['']*int(i())))
for _ in[1]*int(i()):print(l(e,(n:=i())[:-1]+chr(1+ord(n[-1])))-l(e,n))