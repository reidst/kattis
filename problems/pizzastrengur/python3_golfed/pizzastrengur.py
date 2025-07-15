# kattis-accepted
from random import shuffle as s
n=int(input())
*l,='PIZA'
a=''
e=0
while print((a+l[e])[:n],flush=True)or(r:=int(input()))!=2:
 if r:a+=l[e];e=0;s(l)
 elif e==2:a+=l[3];e=0;s(l)
 else:e+=1
