# kattis-accepted
nums = list(map(int, ''.join(input().split('-'))))
mults = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
products = list(map(lambda i: nums[i] * mults[i], range(10)))
if sum(products) % 11:
    print(0)
else:
    print(1)
