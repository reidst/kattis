# kattis-accepted
n, m = map(int, input().split())
nums = [int(num) for num in input().split()]

matches = 0
start = 0
end = m
count = sum(map(lambda n: n % 2 == 0, nums[:m]))
if count >= 2:
    matches += 1

while end < n:
    if nums[start] % 2 == 0:
        count -= 1
    start += 1
    if nums[end] % 2 == 0:
        count += 1
    end += 1

    if count >= 2:
        matches += 1

print(matches)
