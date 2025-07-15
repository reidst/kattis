# kattis-accepted
from bisect import*;l=bisect_left;e=sorted(map(i:=input,' '*int(i())))
for _ in[1]*int(i()):n=i();print(l(e,n[:-1]+chr(1+ord(n[-1])))-l(e,n))
