# kattis-accepted
input()
s = list(input())
delimiters = {')': '(', ']': '[', '}': '{'}
stack = []
for i,c in enumerate(s):
    if c in '([{':
        stack.append(c)
    elif len(stack) == 0 and c in delimiters:
        print(c, i)
        break
    elif c in delimiters:
        if stack[-1] == delimiters[c]:
            stack.pop()
        else:
            print(c, i)
            break
else:
    print('ok so far')
