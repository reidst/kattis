# kattis-accepted
hrs, mins = map(int, input().split())
mins -= 45
if mins < 0:
    mins += 60
    hrs -= 1
if hrs < 0:
    hrs += 24
print(f"{hrs} {mins}")
