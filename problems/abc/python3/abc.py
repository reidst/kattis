def main():
    nums = list(map(int, input().split()))
    nums.sort()
    code = input()
    key = 'ABC'
    output = []
    for letter in code:
        index_in_key = key.index(letter)
        output.append(nums[index_in_key])
    print(*output)


if __name__ == '__main__':
    main()
