lines = []
while (line:=input()) != '-1':
    lines.append(line.split())
correct = [line[1] for line in lines if line[2] == 'right']
lines = [line for line in lines if line[1] in correct]
time_values = [20 if line[2] == 'wrong' else int(line[0]) for line in lines]
print(len(correct), sum(time_values))
