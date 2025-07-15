# kattis-accepted
line, s = input(), []
for char in line:
    s.pop() if char == '<' else s.append(char)
print(''.join(s))
