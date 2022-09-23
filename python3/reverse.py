def main():
    num_lines = int(input())
    nums = []
    for line in range(num_lines):
        nums.append(input())
    nums.reverse()
    for num in nums:
        print(num)


if __name__ == '__main__':
    main()
