# kattis-accepted
row_set = set()
col_set = set()
down_set = set()
up_set = set()

for r in range(8):
    line = input().strip()
    for c in range(8):
        if line[c] == '*':
            row_set.add(r)
            col_set.add(c)
            up_set.add(r - c)
            down_set.add(c + r)

if len(row_set) == len(col_set) == len(down_set) == len(up_set) == 8:
    print("valid")
else:
    print("invalid")
