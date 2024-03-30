_ = input()
nums = list(map(int, input().split()))
last = nums[0]
count = last
for num in nums[1:]:
    count += abs(num - last)
    last = num
print(count)
