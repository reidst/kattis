# kattis-accepted
input()
terraces = list(map(int, input().split()))

total = 0
stack = []

for index, terrace in enumerate(terraces):
    
    while len(stack) > 0 and terrace > stack[-1]['t']:
        stack.pop()

    if len(stack) > 0 and terrace == stack[-1]['t']:
        total += index - stack[-1]['i'] - 1
        stack.pop()
    
    stack.append({'i': index, 't': terrace})


print(total)
