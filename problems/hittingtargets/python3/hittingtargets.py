# kattis-unsolved
def main():
    circs = []
    rects = []
    for _ in range(int(input())):
        shape, *vals = input().split()
        if shape == "rectangle":
            x1, y1, x2, y2 = map(int, vals)
            rects.append((x1, y1, x2, y2))
        else:
            x, y, r = map(int, vals)
            circs.append((x, y, r))
    for _ in range(int(input())):
        x, y = map(int, input().split())
        count = 0
        for circ in circs:
            d_sqr = (x - circ[0]) ** 2 + (y - circ[1]) ** 2
            r_sqr = circ[2] * circ[2]
            if d_sqr <= r_sqr:
                count += 1
        for rect in rects:
            if rect[0] <= x <= rect[2] and rect[1] <= y <= rect[3]:
                count += 1
        print(count)


if __name__ == "__main__":
    main()
