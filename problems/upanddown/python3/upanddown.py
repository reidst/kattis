def main():
    for _ in range(int(input())):
        test()

def lis(nums):
    stacks = []
    longest = []
    for n in nums:
        # find the leftmost stack such that stack.peek >= n
        lo = -1
        hi = len(stacks)
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if stacks[mid][-1] >= n:
                hi = mid
            else:
                lo = mid
        if hi == len(stacks):
            stacks.append([n])
        else:
            stacks[hi].append(n)
        longest.append(hi + 1)
    return longest

def test():
    N = int(input())
    nums = list(map(int, input().split()))
    longest = lis(nums)
    longest_backward = reversed(lis(reversed(nums)))
    best_peak = 0
    for (a, b) in zip(longest, longest_backward):
        if a == 1 or b == 1:
            continue
        this_peak = a + b - 1
        best_peak = max(best_peak, this_peak)
    print(best_peak)


if __name__ == "__main__":
    main()
