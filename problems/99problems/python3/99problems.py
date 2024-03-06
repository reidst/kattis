def main():
    n = int(input())
    larger = int(str(n)[:-2] + '99')
    if n < 100:
        print(larger)
        return
    smaller = int(str((n // 100 - 1) * 100)[:-2] + '99')
    
    if larger - n <= 50:
        print(larger)
    else:
        print(smaller)


if __name__ == '__main__':
    main()
