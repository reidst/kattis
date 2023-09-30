letters = input()
nums = input()

for i in range(len(nums) // 3):
    index = nums[3*i : 3*(i+1)]
    index = int(index)
    print(letters[index-1], end='')