# kattis-partial
_, q = map(int, input().split())
*nums, = sorted(map(int, input().split()))
for row in range(q):
    t, d = map(int, input().split())
    if t == 1:
        # remove smallest n > d, and print n (or -1 if no n)
        for n in nums:
            if n > d:
                print(n)
                nums.remove(n)
                break
        else:
            print(-1)
    else:
        # remove greatest n <= d, and print n (or -1 if no n)
        for n in reversed(nums):
            if n <= d:
                print(n)
                nums.remove(n)
                break
        else:
            print(-1)
