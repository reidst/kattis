# kattis-accepted
from collections import deque
from sys import stdin
lines = stdin.readlines()
first = True
front = deque()
back = deque()
for line in lines:
    if first:
        first = False
        continue
    cmd, x = line.split()
    x = int(x)
    if cmd == 'push_front':
        front.appendleft(x)
        if len(front) - len(back) > 1:
            back.appendleft(front.pop())
    elif cmd == 'push_back':
        back.append(x)
        if len(back) - len(front) > 0:
            front.append(back.popleft())
    elif cmd == 'push_middle':
        if len(front) == len(back):
            front.append(x)
        else:
            back.appendleft(x)
    elif cmd == 'get':
        len_f = len(front)
        if x < len_f:
            print(front[x])
        else:
            print(back[x - len_f])
