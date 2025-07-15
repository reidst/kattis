# kattis-wa
from statistics import mode

def split(l, v):
    ss = []
    start = 0
    for i, u in enumerate(l):
        if u == v:
            ss.append(l[start:i])
            start = i + 1
    ss.append(l[start:])
    return ss

def count(l, free_number):
    if not l:
        return 0
    m = mode(l)
    this_count = 0 if m == free_number else 1
    splits = split(l, m)
    first, *middle, last = splits
    return this_count + count(first + last, free_number) + sum(map(lambda x: count(x, m), middle))

n = int(input())
nums = []
answer = 0

for _ in range(n):
    newnum = int(input())
    nums.append(newnum)

while nums and nums[-1] == 0:
    nums.pop()
start = 0
while start < len(nums) and nums[start] == 0:
    start += 1
nums = nums[start:]

print(count(nums, 0))
