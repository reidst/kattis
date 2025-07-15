# kattis-accepted
def main():
    num_cases = int(input())
    for case in range(num_cases):
        total = list(map(int, input().split()))[1:]
        avg = sum(total)/len(total)
        num_above = 0
        for student in total:
            if student > avg: num_above += 1
        output_val = num_above / len(total) * 100
        print(f'{output_val:.3f}%')


if __name__ == '__main__':
    main()
